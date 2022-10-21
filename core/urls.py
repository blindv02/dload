from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home1'),
    path('home/', views.index, name='home2'),
    path('downloaded/', views.downloaded, name='downloaded'),
    path('done/', views.done, name='done'),
    path('error/', views.error, name='error'),
]
