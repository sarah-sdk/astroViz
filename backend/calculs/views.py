from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Planet

def planet_list(request):
  planets = Planet.objects.all()

  data = [
    {
      "name": planet.name,
      "distance_from_sun": planet.distance_from_sun,
      "diameter": planet.diameter,
      "orbital_period": planet.orbital_period,
    }
    for planet in planets
  ]

  return JsonResponse(data, safe=False)

def interplanetary_age(request):
  try:
    age_earth = float(request.GET.get("age", ""))
  except (TypeError, ValueError):
    return JsonResponse({"error": "Invalid or missing 'age' parameter."}, status=400)
  
  planets = Planet.objects.all()
  result = []

  for planet in planets:
    if planet.name.lower() == "terre":
      result.append({
        "planet": planet.name,
        "age_on_planet": age_earth,
      })
    elif planet.orbital_period > 0:
      age_on_planet = age_earth * ( 365.25 / planet.orbital_period)
      result.append({
        "planet": planet.name,
        "age_on_planet": round(age_on_planet, 2)
      })

  return JsonResponse({"interplanetary_age": result})

def time_to_sun(request):
  light_speed = 299_792  # en km/s

  planet_request = request.GET.get("planet", "").lower()
  if not planet_request:
    return JsonResponse({"error": "Missing 'planet' parameter."}, status=400)
  
  try:
    planet = Planet.objects.get(name__iexact=planet_request)
  except Planet.DoesNotExist:
    return JsonResponse({"error": f"Planet '{planet_request}' not found."}, status=404)
  
  time = round(planet.distance_from_sun * 10**6/ light_speed, 2)

  hours_time = round(time // 3600)
  minutes_time = round((time % 3600) // 60)
  secondes_time = round(time % 60)

  part = []

  if hours_time:
    part.append(f'{hours_time} heure' + ("s" if hours_time > 1 else ""))
  if minutes_time:
    part.append(f'{minutes_time} minute' + ("s" if minutes_time > 1 else ""))
  if secondes_time:
    part.append(f'{secondes_time} seconde' + ("s" if secondes_time > 1 else ""))

  return JsonResponse({"time_to_sun": " ".join(part)})


