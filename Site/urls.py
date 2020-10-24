from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='index'),
    path('details/', views.details, name='details'),
]