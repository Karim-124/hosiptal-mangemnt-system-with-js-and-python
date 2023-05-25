from django.shortcuts import render ,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # Create your views here.
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    Doctor_user = Doctor.objects.get(user=request.user)
    return render(request, 'dr_dashbord.html',{'Doctor':Doctor_user})


@login_required(login_url='login')
def profile(request):
    Doctor_user = Doctor.objects.get(user=request.user)
    if request.method == "POST":
        form = ProfileDoctor(request.POST , request.FILES ,  instance = Doctor_user)
        if form.is_valid:
            form.save()
            return redirect('/Doctor/Dashboard')
    else:
        form = ProfileDoctor(instance = Doctor_user)
    return render(request, 'myprofile.html',{'form':form,'Doctor':Doctor_user})

@login_required(login_url='login')
def myAppointment(request):
    Doctor_user = Doctor.objects.get(user=request.user)
    Doctor_Appointment = Appointment.objects.all().filter(doctor=Doctor_user)
    return render(request, 'myappointment.html',{'Doctor':Doctor_user,'Data_Appointment':Doctor_Appointment})


@login_required(login_url='login')
def patientslist(request):
    Doctor_user = Doctor.objects.get(user=request.user)
    patient_Appointment=Appointment.objects.all().filter(doctor=Doctor_user)
    return render(request, 'patient.html',{'Doctor':Doctor_user,'Data_Appointment':patient_Appointment})


@login_required(login_url='login')  
def deletbook(request,id):
    Appointment.objects.get(id = id).delete()
    return redirect('/Doctor/patients') 

@login_required(login_url='login')  
def descrption_write(request,id):
    Doctor_user = Doctor.objects.get(user=request.user)
    if request.method == "POST":
        descrption_write = request.POST.get('descrption')
        created_descrption = Appointment.objects.get(id = id)
        created_descrption.descrption = descrption_write
        created_descrption.save() 
        return redirect('/Doctor/patients') 
    return render(request, 'descrption-form-write.html',{'Doctor':Doctor_user} )
    
