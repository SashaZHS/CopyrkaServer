from rest_framework import serializers
from profile_imgs.models import Image


class ImageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields = '__all__'
