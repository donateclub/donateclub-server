from django.urls import path,include
from .views import *
from .serializers import *

urlpatterns = [
    path('products/', product_collection, name='product_collection'),
    path('ngos/', ngo_collection, name='ngo_collection'),
    path('issues/', issues_collection, name='issues_collection'),
    path('posts/', blog_post_collection, name='blog_post_collection'),
    path('doantions/', donation_collection, name='donation_collection'),
    path('badges/', badge_collection, name='badge_collection'),
    path('services/', service_collection, name='service_collection'),
    path('users/', user_collection, name='user_collection'),
]
