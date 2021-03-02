# god101
from django.db import models
from django.contrib.auth.models import AbstractUser

class Ngo(models.Model):
    title = models.CharField(verbose_name="Title" , max_length=64)
    description = models.CharField(verbose_name="Description" , max_length=255)

class Category(models.Model):
    name =  models.CharField(verbose_name="Category" , max_length=64)

class Product(models.Model):
    title = models.CharField(verbose_name="Title" , max_length=64)
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

# class ClubUser(AbstractUser):
#     pass