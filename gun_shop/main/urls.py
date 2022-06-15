from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('FAQ', views.FAQ),
    path('about', views.about)
]
