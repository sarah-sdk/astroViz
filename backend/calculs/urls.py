from django.urls import path
from . import views

urlpatterns = [
  path('planets/', views.planet_list, name='planet_list'),
  path('interplanetary-age/', views.interplanetary_age, name="interplanetary_age"),
  path('time-to-sun/', views.time_to_sun, name='time_to_sun')
]