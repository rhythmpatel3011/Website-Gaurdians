from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .support import send_otp_to_phone
from .forms import *
from .models import *
from qrcode import *
import time
from django.conf import settings
import random
# Create your views here.
def Register(request):
    if request.method != "POST":
        return render(request, "register.html")
    username = request.POST['username']
    email = request.POST['email']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 != password2:
        messages.error(request, "Passwords do not match.")
        return redirect('/register')

    user = User.objects.create_user(username, email, password1)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    return render(request, 'login.html')

def Login(request):
    if request.method != "POST":
        return render(request, "new_login.html")
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        messages.success(request, "Successfully Logged In")
        return redirect('/number_verification')
    else:
        messages.error(request, "Invalid Credentials")
    return redirect('/login')


def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login')

def home(request):
    return render(request, 'frontend_page.html')


def number_verification(request):
    if request.method == "POST":
        fm = num_status(request.POST)
        if fm.is_valid():
            # reg = number(phone_number=fm.cleaned_data['phone_number'])
            # reg.save()
            # get_num=number(phone_number=fm.cleaned_data['phone_number'])
            get_num = fm.cleaned_data['phone_number']
            print(get_num)
            get_otp = send_otp_to_phone(get_num)
            print(get_otp)
            reg = otp_verify(otp=get_otp)
            reg.save()
            return redirect('/otp')
    else:
        fm = num_status()
    return render(request ,'number_verification.html',{'form': fm})

def otp_verification(request):  # sourcery skip: assign-if-exp
    get_otp = otp_verify.objects.all().values_list('otp', flat=True)
    list_otp = list(get_otp)
    if request.method == "POST":
        fm = final_otp_status(request.POST)
        if fm.is_valid():
            reg = fm.cleaned_data['f_otp']
            if reg in list_otp:
                return redirect('/qr_code')
            else:
                return render(request, 'not_verified.html')
    else:
        fm = final_otp_status()
    return render(request ,'otp.html',{'form': fm})

def qr_gen(request):  # sourcery skip: assign-if-exp, remove-unreachable-code
    otp = random.randint(1000, 9999)
    fotp=qr_code(qr_code_value=otp)
    fotp.save()
    all_data = qr_code.objects.all().values_list('qr_code_value', flat=True)
    list_otp = list(all_data)
    img = make(otp)
    print(otp)
    img_name = f'qr{str(time.time())}.png'
    img.save(f'{settings.MEDIA_ROOT}/{img_name}')
    if request.method == "POST":
        fm = qr_code_status(request.POST)
        if fm.is_valid():
            reg = fm.cleaned_data['qr_code_value']
            print(otp)
            if reg in list_otp:
                print(otp)
                return redirect('/upload')
            else:
                print(otp)
                return render(request, 'not_verified.html')
    else:
        fm = qr_code_status()
    return render(request, 'qr.html', {'img_name': img_name,'form':fm})

def face_detect(request):
    fm = upload_status()
    if request.method == "POST":
        if fm.is_valid():
            reg = upload(upload_file=fm.cleaned_data['upload_file'])
            reg.save()
            
    else:
        fm = upload_status()
    return render(request, 'upload.html', {'form':fm})

def verify(request):
    return render(request, 'verified.html')