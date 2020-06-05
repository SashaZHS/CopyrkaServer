from django.urls import path, include
from profile_imgs.views import ImageListView, ImageCreateView, ImageDetailView
import djoser.views
import djoser.urls

urlpatterns = [
    path('image/create/',ImageCreateView.as_view()),
    path('all/',ImageListView.as_view()),
    path('image/<int:pk>/',ImageDetailView.as_view()),

]