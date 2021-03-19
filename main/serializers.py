from rest_framework import serializers
from .models import *

class NgoSerializer(serializers.ModelSerializer):

    year_established = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = Ngo
        fields = ('pk', 'title', 'rating', 'year_established', 'description', 'country', 'state', 'city', 'pincode', 'issue', 'phone_number', 'email')

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('pk','name', 'description')
    
class ProductSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = Product
        fields = ('pk', 'title', 'description', 'deadline', 'required', 'donated', 'issue', 'ngo', 'image')

class BlogPostSerializer(serializers.ModelSerializer):
    date_published = serializers.DateTimeField(format="%Y-%m-%d")
    date_edited = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = BlogPost
        fields = ('pk','title', 'date_published', 'date_edited', 'body', 'ngo','issue')

class DonationSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = Donation
        fields = ('pk', 'date', 'amount', 'user', 'product')

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ('pk', 'title', 'description','threshold')

class ServiceSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(format="%Y-%m-%d")
    end_date = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = Service
        fields = ('pk', 'title', 'description', 'start_date', 'end_date', 'paid', 'salary', 'image', 'ngo', 'issue')

class ClubUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubUser
        fields = ('pk', 'username', 'image', 'email', 'phone_number', 'country', 'state', 'city')