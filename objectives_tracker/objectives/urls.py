from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='objectives-home'),
    path('home/', views.home, name='objectives-home')
]
