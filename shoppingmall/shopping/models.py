from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    price = models.CharField(max_length=500)
    image = models.ImageField(upload_to = "shopping/", blank=True, null=True)

    def __str__(self) :
        return self.name