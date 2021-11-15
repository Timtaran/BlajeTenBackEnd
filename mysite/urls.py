"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views
from . import pywebio_code
from pywebio.platform.django import webio_view

# `task_func` is PyWebIO task function
webio_view_func = webio_view(pywebio_code.bmi)
webio_view_func2 = webio_view(pywebio_code.MSM)
urlpatterns = [
  path(r"tool", webio_view_func),
    path('admin/', admin.site.urls),
    path('register_new_acc/<str:name>/<str:password>/<str:password2>', views.register),
    path('login/', views.login),
    path('login/<str:name>/<str:password>/', views.login),
    path('register_new_acc/', views.register),
    path('sr/<str:name>', views.sr),
    path('er/', views.er),
    path('register/', views.register_page),
    path('api_login/', views.api_login),
    path('api_data/', views.api_data),
    path('gd/<str:name>', views.gd),
    path('gd/', views.gd),
    path(r"minescale", webio_view_func2),
    path('', views.index)    
]