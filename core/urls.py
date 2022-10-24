from django.urls import path, include
from . import views


urlpatterns = [
    path('home1/', views.index, name='home1'),
    path('home/', views.index, name='home2'),
    path('downloaded/', views.downloaded, name='downloaded'),
    path('done/', views.done, name='done'),
    path('error/', views.error, name='error'),
    path('', views.login, name='login'),
    path('registrar/', views.registrar, name='registrar'),
]
