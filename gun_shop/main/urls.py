from django.urls import path
from gun_shop.main import views

urlpatterns = [
    path('', views.index),
    path('about', views.about)
]
