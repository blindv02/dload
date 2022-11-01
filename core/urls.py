from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home1'),
    path('home/', views.index, name='home2'),
    path('downloaded/', views.downloaded, name='downloaded'),
    path('done/', views.done, name='done'),
    path('error/', views.error, name='error'),
    path('search/', views.search, name='search'),
    path('search_list/', views.search_list, name='search_list'),
    path('dwnmp3/', views.downmp3, name='downmp3'),
    path('dwnmp4/', views.downmp4, name='downmp4'),
    #path('login/', views.login, name='login'),
    #path('registrar/', views.registrar, name='registrar'),
]
