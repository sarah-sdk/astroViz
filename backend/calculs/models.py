from django.db import models

# Create your models here.
class Planet(models.Model):
  name = models.CharField(max_length=100)
  distance_from_sun = models.FloatField()    # en millions de km
  diameter = models.FloatField()             # en km
  orbital_period = models.FloatField()       # en jours

  def __str__ (self):
    return self.name
