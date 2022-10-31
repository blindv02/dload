from django.urls import path
from . import views
from .models import *

urlpatterns = [
    path('registrar/', views.registrar, name='registrar'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
