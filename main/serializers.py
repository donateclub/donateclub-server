from rest_framework import serializers
from .models import *

class NgoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ngo
        fields = ('pk','title', 'description')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk','name',)
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk','ngo', 'category')