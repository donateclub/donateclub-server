# god101
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Issue(models.Model):
    name =  models.CharField(verbose_name="Issue" , max_length=64)
    description = models.TextField(verbose_name="Description")

class Ngo(models.Model):
    title = models.CharField(verbose_name="Title" , max_length=64)
    rating = models.IntegerField()
    year_established = models.DateField()
    description = models.TextField(verbose_name="Description")
    country = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    pincode = models.CharField(max_length=64)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(max_length=254)

class Product(models.Model):
    title = models.CharField(verbose_name="Title" , max_length=64)
    description = models.TextField(verbose_name="Description")
    deadline = models.DateTimeField()
    required = models.IntegerField()
    donated = models.IntegerField()
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    
class Service(models.Model):
    title = models.CharField(verbose_name="Title" , max_length=64)
    description = models.TextField(verbose_name="Description")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    paid = models.BooleanField()
    salary = models.BigIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

class BlogPost(models.Model):
    title = models.CharField(max_length=64)
    date_published = models.DateTimeField()
    date_edited = models.DateTimeField()
    body = models.TextField(verbose_name="Body")
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

# class ClubUser(AbstractUser):
#     pass