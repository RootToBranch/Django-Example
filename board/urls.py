from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('test/', views.test),
    path('signup/', views.signup)
]
