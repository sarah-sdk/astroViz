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
