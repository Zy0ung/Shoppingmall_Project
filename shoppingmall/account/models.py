from django.db import models
from django.contrib.auth.models import AbstractUser
from shopping.models import Item

# Create your models here.
class User(AbstractUser):
    university = models.CharField(max_length=50)
    adress = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "account/", blank=True, null=True)

class Order(models.Model):
    order_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.order_item.name