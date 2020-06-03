from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Image(models.Model):
    profile_pic = models.ImageField(verbose_name='image', default='default_profile_img.jpg', null=True, blank=True)
    is_profile_pic = models.BooleanField(verbose_name='is_profile',default=False)
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)


