from django.urls import path,include
from .views import *
from .serializers import *

urlpatterns = [
    path('products/', product_collection, name='product_collection'),
    path('ngos/', ngo_collection, name='ngo_collection'),
    path('cats/', category_collection, name='category_collection'),
]
