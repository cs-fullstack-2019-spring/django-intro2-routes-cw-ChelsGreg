from django.urls import path

from . import views


# DIRECTING ROUTES TO FUNCTIONS
urlpatterns = [
    path('', views.index, name='index'),
    path('gogetthegood/', views.getTheGood, name='index'),
    path('happyhappyjoyjoy/', views.happyHappy, name='index'),


]