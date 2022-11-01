from cgitb import html
from multiprocessing import context
from turtle import title
from unicodedata import name
from django.shortcuts import render, HttpResponse, redirect
from pytube import YouTube
from pytube import Search
import os
from os import path, rename, remove
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='')
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

@login_required(login_url='')
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

@login_required(login_url='')
def error(request):
    return render(request, 'error.html')

@login_required(login_url='')
def search(request):
    return render(request, 'search.html')

@login_required(login_url='')
def search_list(request):
    ustr = request.GET.get('url')
    s = Search(ustr)    
    return render(request, 'search.html',{'resultado': s.results})


@login_required(login_url='')
def downmp3(request):
        global vurl3
        vurl3 = request.GET.get('vurl3')
        homedir = os.path.expanduser("~\Downloads")
        ytb = YouTube(vurl3)
        video = YouTube(vurl3).streams.get_audio_only().download(homedir)
        base, ext = path.splitext(video)
        new_file = base + '.mp3'
        rename(video, new_file)
        
        try:    
            with open(new_file, 'rb') as f:
                file_data = f.read()

            # sending response 
            response = HttpResponse(file_data, content_type='audio/mpeg')
            response['Content-Disposition'] = 'attachment; filename="'+ ytb.title +'.mp3"'
            
        except IOError:
            # handle file not exist case here
            response = HttpResponseNotFound(request, 'error.html')
            
        os.remove(new_file)
        return response


@login_required(login_url='')
def downmp4(request):
        global vurl4
        vurl4 = request.GET.get('vurl4')
        ytb = YouTube(vurl4)
        homedir = os.path.expanduser("~\Downloads")
        video = YouTube(vurl4).streams.filter(file_extension='mp4').get_highest_resolution().download(homedir)
        base, ext = path.splitext(video)
        new_file = base + '.mp4'
        rename(video, new_file)
        
        try:    
            with open(new_file, 'rb') as f:
                file_data = f.read()

            # sending response 
            response = HttpResponse(file_data, content_type='video/mp4')
            response['Content-Disposition'] = 'attachment; filename="'+ ytb.title +'.mp4"'
        
        except IOError:
            # handle file not exist case here
            response = HttpResponseNotFound(request, 'error.html')
            
        os.remove(new_file)
        return response