from rest_framework import serializers
from .models import *

class NgoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ngo
        fields = ('pk', 'title', 'rating', 'year_established', 'description', 'country', 'state', 'city', 'pincode', 'issue', 'phone_number', 'email')

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('pk','name', 'description')
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'title', 'description', 'deadline', 'required', 'donated', 'issue', 'ngo', 'image')

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('pk','title', 'date_published', 'date_edited', 'body', 'ngo','issue')

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ('pk', 'date', 'amount', 'user', 'product')

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = badge
        fields = ('pk', 'title', 'description','threshold')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('pk', 'title', 'description', 'start_date', 'end_date', 'paid', 'salary', 'image', 'ngo', 'issue')

class ClubUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubUser
        fields = ('pk', 'username', 'image', 'email', 'phone_number', 'country', 'state', 'city')