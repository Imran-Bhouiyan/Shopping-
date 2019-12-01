from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
        
    def __str__(self):
        return f'{self.user.username} Customer '


class UserProfile(models.Model):
    pass


class Order(models.Model):
    pass

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField()



CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport 