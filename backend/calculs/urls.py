from django.urls import path
from . import views

urlpatterns = [
  path('planets/', views.planet_list, name='planet_list'),
]