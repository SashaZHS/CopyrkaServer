from django.shortcuts import render
from rest_framework import generics
from profile_imgs.serializers import *
from profile_imgs.models import Image
from rest_framework.permissions import IsAdminUser
from profile_imgs.permissions import IsOwner
from rest_framework.response import Response


# Create your views here.
class ImageCreateView(generics.CreateAPIView):
    serializer_class = ImageDetailSerializer


class ImageListView(generics.ListAPIView):
    serializer_class = ImageListSerializer
    queryset = Image.objects.all()


class ImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageDetailSerializer
    queryset = Image.objects.all()