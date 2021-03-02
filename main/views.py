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
def category_collection(request):
    if request.method == 'GET':
        cats = Category.objects.all()
        serializer = CategorySerializer(cats, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def product_collection(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)