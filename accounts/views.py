from datetime import datetime
from telnetlib import STATUS
from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
#from .models import accounts
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.db.models import Q
from django.http import HttpResponse 
import json
from django.contrib.auth import login, authenticate

from django.core.mail import send_mail
import smtplib
import ssl
from email.message import EmailMessage



# Create your views here.
def registrar(request):
    form = RegistroForm()
    
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        #print("registro")
        if form.is_valid():
            #print("registro valido")
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = Usuario.objects.create_user(nombre=nombre, apellido=apellido, email=email, password=password)
            user.save()
            messages.success(request, 'Se guardo el usuario!')
            return redirect('login')

    context = {
        'form': form
    }

    return render(request, 'registrar.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        #print("El user es =", user)
        if user is not None:
           #print("hay usu")   
            auth.login(request, user)
            messages.success(request, 'Has iniciado sesion exitosamente')
            context={
                'usuario':user,
            }
            return render(request,'index.html',context)
        else:
            print("mal contraseña")
            if Usuario.objects.filter(email=email).exists():
                user=Usuario.objects.filter(email=email).first()
                messages.error(request, 'La contraseña es incorrecta!')
                return redirect('login')
            else:    
                print("No existe el Usuario")
                messages.error(request, 'No existe el usuario')
                return redirect('login')
    user=auth.authenticate(email=None, password=None)
    context={
           'usuario':user
            }
    print(context)
    return render(request, 'login.html',context)


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.warning(request, 'Has salido de sesion')
    return redirect('login')



