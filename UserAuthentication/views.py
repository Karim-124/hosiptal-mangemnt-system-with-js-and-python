from django.shortcuts import render, redirect
from .forms import CreateNewUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from patient.models import Patient
from django.contrib.auth.models import User
from django.db.models import *
from .models import *
from doctor.models import Doctor
from manager.models import Manager

# Create your views here.
def home(request):
    all_doctor=Doctor.objects.all()
    return render(request,'index.html',{'all_doctor':all_doctor})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username , password =password)
        if user is not None:
            patient_user = Patient.objects.filter(user=user).first()
            doctor_user = Doctor.objects.filter(user=user).first()
            manager_user = Manager.objects.filter(user=user).first()
            if patient_user is not None:
               # messages.info(request,patient_user)
               login(request, user)
               return redirect('/Patient/Dashboard')
            elif doctor_user is not None:
                # messages.info(request, doctor_user)
                login(request, user)
                return redirect('/Doctor/Dashboard')
            else:
                # messages.info(request, manager_user)
                login(request, user)
                return redirect('/Manager/Dashboard')
                
        else:
            messages.info(request , "Invaild username or password")
    return render(request , 'login.html')

def register(request):
    
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            form.save()
            Patient.objects.create(user=user).save()
            return redirect('login')
    else:
          form = CreateNewUser()


    return render(request , 'signup.html' , {'form': form})
def sinout(request):
    logout(request)
    return redirect('home')