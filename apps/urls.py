"""dproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf path('update/<int:id>/', views.update_student),
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from graphviz import view
from apps import views
from rest_framework import routers

router = routers.SimpleRouter()

router.register('Book', views.BookView, basename='Book')
router.register('Admin', views.AdminView, basename='Admin')
from .views import *

urlpatterns = [
    path('', include(router.urls)),
    path('',views.welcome),
    path('signup/',views.signup),
    path('signupsucess/', views.signup_success),
    path('signupfaild/', views.signup_faild),
    path('login/', views.login),
    path('loginfaild/', views.loginfaild),
    path('show/', views.show),
    path('add/', views.addbook),
    path('update/<int:id>/', views.update),
    path('delete/<int:id>/', views.delete_book)



]
