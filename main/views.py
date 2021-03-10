from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET'])
def ngo_collection(request):
    if request.method == 'GET':
        ngos = Ngo.objects.all()
        serializer = NgoSerializer(posts, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def issues_collection(request):
    if request.method == 'GET':
        cats = Issue.objects.all()
        serializer = IssueSerializer(cats, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def product_collection(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def blog_post_collection(request):
    if request.method == 'GET':
        posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(posts, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def donation_collection(request):
    if request.method == 'GET':
        donations = Donation.objects.all()
        serializer = DonationSerializer(donations, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def badge_collection(request):
    if request.method == 'GET':
        badges = Badge.objects.all()
        serializer = BadgeSerializer(badges, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def service_collection(request):
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def user_collection(request):
    if request.method == 'GET':
        users = ClubUser.objects.all()
        serializer = ClubUserSerializer(users, many=True)
        return Response(serializer.data)