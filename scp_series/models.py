from django.db import models
from django.core.validators import MaxValueValidator

class Object(models.Model):
  CLASS_CHOICES = [
      ('Safe', 'Safe'),
      ('Euclid', 'Euclid'),
      ('Keter', 'Keter'),
      ('Thaumiel', 'Thaumiel'),
      ('Neutralized', 'Neutralized'),
      ('Explained', 'Explained'),
      ('Esoteric/Narrative', 'Esoteric/Narrative'),
      ('Decommissioned', 'Decommissioned'),
  ]
  item = models.PositiveIntegerField(
      validators=[MaxValueValidator(5999)], unique=True, primary_key=True)
  object_class = models.CharField(
      max_length=18, choices=CLASS_CHOICES, default="SF")
  containment_procedures = models.TextField()
  description = models.TextField()
  additional = models.TextField(blank=True)

