from cgitb import html
from multiprocessing import context
from turtle import title
from unicodedata import name
from django.shortcuts import render, HttpResponse, redirect
from pytube import YouTube
import os
from os import path, rename, remove
from django.http import HttpResponse, HttpResponseNotFound

# Importamos la clase Usuarios
from .models import Usuarios
# Importamos el Form UsuariosForm
from .forms import UsuariosForm

# importamos estas librerias para control de usuarios y mensajes
from django.contrib import messages, auth

# Create your views here.

def index(request):
    user = request.user
    context={'user':user}
    return render(request, 'index.html',context)

def downloaded(request):
    global url, yt
    url = request.GET.get('url')
    y = 'youtube.com/watch?v='
    
    if y.lower() not in url:
        return render(request, 'error.html')
    
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True, progressive=False)
    embed_link = url.replace('watch?v=', 'embed/')
    title = yt.title
    context = {'video': video,'embed': embed_link,'title': title}

    return render(request, 'downloaded.html', context)

def done(request):
    global url
    homedir = os.path.expanduser("~\Downloads")
    button_type1 = request.POST.get("bttn1")
    button_type2 = request.POST.get("bttn2")
    
    if button_type2 == 'mp3':
        video = YouTube(url).streams.get_audio_only().download(homedir)
        base, ext = path.splitext(video)
        new_file = base + '.mp3'
        rename(video, new_file)
        
        try:    
            with open(new_file, 'rb') as f:
                file_data = f.read()

            # sending response 
            response = HttpResponse(file_data, content_type='audio/mpeg')
            response['Content-Disposition'] = 'attachment; filename="'+ yt.title +'.mp3"'
            
        except IOError:
            # handle file not exist case here
            response = HttpResponseNotFound(request, 'error.html')
            
        os.remove(new_file)
        return response
    
    elif button_type1 == 'mp4':
        video = YouTube(url).streams.filter(file_extension='mp4').get_highest_resolution().download(homedir)
        base, ext = path.splitext(video)
        new_file = base + '.mp4'
        rename(video, new_file)
        
        try:    
            with open(new_file, 'rb') as f:
                file_data = f.read()

            # sending response 
            response = HttpResponse(file_data, content_type='video/mp4')
            response['Content-Disposition'] = 'attachment; filename="'+ yt.title +'.mp4"'
        
        except IOError:
            # handle file not exist case here
            response = HttpResponseNotFound(request, 'error.html')
            
        os.remove(new_file)
        return response
    else:
        return render(request, 'error.html')

def error(request):
    return render(request, 'error.html')

def login(request):
    if request.method == 'POST':
        #recuperamos el valor de los campos
        email = request.POST['email']
        password = request.POST['password']

        user = Usuarios.objects.filter(email=email,password=password).first()
        print("El user es =", user)
        if user is not None:
            print("Hizo Login!!!")
            messages.success(request, 'Has iniciado sesion exitosamente')
            context={
                'usuario':user,
            }
            return render(request,'index.html',context)
        else: #No encontro usuario usuario y contraseña
            
            if Usuarios.objects.filter(email=email).exists():
                
                user=Usuarios.objects.filter(email=email).first()
                print("email=" +email)
                messages.error(request, 'La contraseña es incorrecta')
                
            else:    
                print("no hay usu")
                messages.error(request, 'El Usuario no existe')
            return redirect('login')
        
    return render(request, 'login.html')

def registrar(request):
    form = UsuariosForm()
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre',"")
        apellido = request.POST.get('apellido',"")
        if nombre == "" or apellido == "":
            messages.warning(request, 'No ingreso Nombre y/o apellido')
            return redirect('registrar')
                     
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    #Le pasamos el form vacio para que se renderice en el register.html
    context = {
        'form': form
    }

    return render(request, 'registrar.html', context)
