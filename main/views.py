from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

from rest_framework import status, generics


class NgoList(generics.ListCreateAPIView):
    queryset = Ngo.objects.all()
    serializer_class = NgoSerializer

class NgoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ngo.objects.all()
    serializer_class = NgoSerializer


class IssuesList(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class IssueDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BlogsList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class DonationsList(generics.ListCreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

class DonationDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

class BadgesList(generics.ListCreateAPIView):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer

class BadgeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer

class ServicesList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ClubUsersList(generics.ListAPIView):
    queryset = ClubUser.objects.all()
    serializer_class = ClubUserSerializer

class ClubUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClubUser.objects.all()
    serializer_class = ClubUserSerializer