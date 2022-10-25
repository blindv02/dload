"""Dloader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from distutils import core
from operator import index
from unicodedata import name
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
import core.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core.views.index, name='home1'),
    path('home/', core.views.index, name='home2'),
    path('downloaded/', core.views.downloaded, name='downloaded'),
    path('done/', core.views.done, name='done'),
    path('error/', core.views.error, name='error'),
    path('search/', core.views.search, name='search'),
    path('search_list/', core.views.search_list, name='search_list'),
    path('dwnmp3/', core.views.downmp3, name='downmp3'),
    path('dwnmp4/', core.views.downmp4, name='downmp4'),
    
]
