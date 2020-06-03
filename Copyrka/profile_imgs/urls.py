from django.urls import path, include
from profile_imgs.views import *

urlpatterns = [
    path('image/create/',ImageCreateView.as_view())
]