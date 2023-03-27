from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path("accounts/", include("django.contrib.auth.urls")), # new
    path('upload/', views.loadImage, name='upload'),
]