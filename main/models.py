# god101
# user101
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
import os
import datetime

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Issue(models.Model):
    name =  models.CharField(verbose_name="Issue" , max_length=64)
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return f"{self.name}"

class Ngo(models.Model):
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    title = models.CharField(verbose_name="Title" , max_length=64)
    rating = models.IntegerField()
    year_established = models.DateTimeField()
    description = models.TextField(verbose_name="Description")
    country = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    pincode = models.CharField(max_length=64)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(max_length=254)
    site = models.CharField(verbose_name="Web Site" , max_length=64)

    def __str__(self):
        return f"{self.title}"

class ClubUser(AbstractUser):
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    email = models.EmailField(max_length=254)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    country = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    city = models.CharField(max_length=64)

class Product(models.Model):
    owner = models.ForeignKey(ClubUser, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title" , max_length=64)
    description = models.TextField(verbose_name="Description")
    deadline = models.DateTimeField()
    required = models.IntegerField()
    donated = models.IntegerField()
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):

        super(Product, self).save(*args, **kwargs)

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

    def __str__(self):
        return f"{self.title}"

class BlogPost(models.Model):
    title = models.CharField(max_length=64)
    date_published = models.DateTimeField()
    date_edited = models.DateTimeField()
    body = models.TextField(verbose_name="Body")
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class Donation(models.Model):
    date = models.DateTimeField()
    amount = models.IntegerField()
    user = models.ForeignKey(ClubUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}"

class Badge(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(verbose_name="Description")
    threshold = models.IntegerField()
    
    def __str__(self):
        return f"{self.title}"

class UserBadge(models.Model):
    user = models.ForeignKey(ClubUser, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)

class ContactUs(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=255)
    message = models.TextField(verbose_name="Message")