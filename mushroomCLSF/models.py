from django.db import models

# Create your models here.

class MushroomData(models.Model):
    cap_shape = models.CharField(max_length=5)
    cap_surface = models.CharField(max_length=5)
    cap_color = models.CharField(max_length=5)
    bruises = models.CharField(max_length=5)
    odor = models.CharField(max_length=5)
    stalk_shape = models.CharField(max_length=5)
    stalk_root = models.CharField(max_length=5)
    spore_print_color = models.CharField(max_length=5)
    habitat = models.CharField(max_length=5)
    population = models.CharField(max_length=5)
    ring_type = models.CharField(max_length=5)

    def to_json(self):
        return {
            "cap_shape": self.cap_shape,
            "cap_surface": self.cap_surface,
            "cap_color": self.cap_color,
            "bruises": self.bruises,
            "odor": self.odor,
            "stalk_shape": self.stalk_shape,
            "stalk_root": self.stalk_root,
            "spore_print_color": self.spore_print_color,
            "habitat": self.habitat,
            "population": self.population,
            "ring_type": self.ring_type
        }

