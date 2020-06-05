from rest_framework import serializers
from profile_imgs.models import Image
import djoser.views

class ImageDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Image
        fields = '__all__'


class ImageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


