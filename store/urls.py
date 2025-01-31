"""
URL configuration for myresturant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('signup', views.signup, name= 'signup'),
    path('menu', views.menu, name= 'menu'),
    path('front', views.front, name= 'front'),
    path('signinpage', views.signinpage, name= 'signinpage'),
    path('logout', views.logout, name= 'logout'),
    path('cart1', views.cart1, name= 'cart1'),
    path('checkout', views.checkout, name= 'checkout'),
    path('orderNow', views.orderNow, name= 'orderNow'),
     path('ContactUs', views.ContactUs, name= 'ContactUs'),


]
