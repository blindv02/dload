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
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
import accounts  
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
    return render(request, 'login.html',context)


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.warning(request, 'Has salido de sesion')
    return redirect('login')


##INCORPORAMOS EL OLVIDE MI CONTRASEÑA###
def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Usuario.objects.filter(email=email).exists():
            user = Usuario.objects.get(email__exact=email)

            current_site = get_current_site(request)

            # Configuracion de los mails
            email_sender = 'codoacodogrupo2@gmail.com'
            email_password = 'nehzreldzquvgshy' #esta es la contraseña global de gmail para este mail
            email_receiver = email
            # configuramos el mail 
            subject = 'Por favor resetea tu password en dload!'
            body = render_to_string('reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token': default_token_generator.make_token(user),
            })

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            # Add SSL (layer of security)
            context = ssl.create_default_context()

            # Log in and send the email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
                print(body)
            messages.success(request, 'Un email fue enviado a tu bandeja de entrada para resetear tu password')
            return redirect('login')
        else:
            messages.error(request, 'La cuenta de usuario no existe')
            return redirect('forgotPassword')

    return render(request, 'forgotPassword.html')

def resetpassword_validate(request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = Usuario._default_manager.get(id=uid)
            print(uid,'User ID')
            print(user,'Este es el usuario')
        except(TypeError, ValueError, OverflowError, Usuario.DoesNotExist):
            user=None

        if user is not None and default_token_generator.check_token(user, token):
            request.session['uid'] = uid
            messages.success(request, 'Por favor resetea tu password')
            return redirect('resetPassword')
        else:
            messages.error(request, 'El link ha expirado')
            return redirect('login')

def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Usuario.objects.get(id=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'El password se reseteo correctamente')
            return redirect('login')
        else:
            try:
                messages.error(request, 'El password de confirmacion no concuerda')
                return redirect('resetPassword')
            except:
                print('aqui es donde da el error')
    else:
        return render(request, 'resetPassword.html')
        