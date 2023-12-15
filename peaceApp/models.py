from django.db import models

class Charities(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name