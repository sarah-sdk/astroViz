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
