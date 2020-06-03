from django.shortcuts import render
from rest_framework import generics
from profile_imgs.serializers import ImageDetailSerializer
from profile_imgs.permissions import IsOwner
from rest_framework.permissions import IsAdminUser


# Create your views here.
class ImageCreateView(generics.CreateAPIView):
    serializer_class = ImageDetailSerializer
