from rest_framework import serializers
from .models import *

class NgoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ngo
        fields = ('pk','title', 'description')

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('pk','name',)
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk','ngo', 'issue')