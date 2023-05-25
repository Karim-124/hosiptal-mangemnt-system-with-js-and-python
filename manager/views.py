from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import * 
from doctor.models import *
from patient.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from doctor.forms import *


# Create your views here.
@login_required(login_url='login')
def Dashboard(request):
   manager_user =  Manager.objects.get(user=request.user)
   Total_User   = User.objects.all().count()
   Total_Doctor=  Doctor.objects.all().count()
   Total_Patient = Patient.objects.all().count()
   Total_Appointment = Appointment.objects.all().count()
   Total_Specialization =Specialization.objects.all().count()
   return render(request,'manager/dashbord.html',{'manager_user':manager_user,'Total_Doctor':Total_Doctor,'Total_Patient':Total_Patient,'Total_Appointment':Total_Appointment,'Total_User':Total_User,'Total_Specialization':Total_Specialization})

@login_required(login_url='login')
def AddDoctor(request):
   manager_user =Manager.objects.get(user=request.user)
   form = CreationDoctor()
   if request.method == 'POST':
      form = CreationDoctor(request.POST)
      if form.is_valid(): 
            form.save() 
            return redirect('/Manager/Dashboard')
   context = {
      'form' : form,
      'errors' : form.errors,
    'manager_user':manager_user
   }    
   return render(request,'manager/add-doctor.html',context)

@login_required(login_url='login')
def AddUser(request):
   manager_user =Manager.objects.get(user=request.user)
   form = CreationUser()
   if request.method == 'POST':
      form = CreationUser(request.POST)
      if form.is_valid():
            form.save()
            return redirect('/Manager/Dashboard')  
   context = {
      'form' : form,
      'errors' : form.errors,
       'manager_user': manager_user
   }    
   return render(request,'manager/add-user.html',context)    
    
@login_required(login_url='login')
def AddSpecification(request):
   form = Creationspecification()
   manager_user = Manager.objects.get(user=request.user)
   if request.method == 'POST':
      form = Creationspecification(request.POST)
      if form.is_valid():
        form.save()
        return redirect('/Manager/Dashboard')  
   context = {
   'form' : form,
   'errors' : form.errors,
    'manager_user':manager_user
   }    
   return render(request,'manager/add-specification.html',context)
    
@login_required(login_url='login')
def myAppointment(request):
   Appointment_list = Appointment.objects.all()
   manager_user = Manager.objects.get(user=request.user)
   # Appointment_search_list=[]
   # if  request.method == 'POST':
   #     Appointment_search =request.POST.get('Appointment_Search', False)
   #     Appointment_search_list.append(Appointment.objects.filter(name__icontains=Appointment_search))
   #     Appointment_search_list.append(Appointment.objects.filter(data_time__icontains=Appointment_search))
   #     return render(request, 'manager/appointment.html',
   #                   {'Appointment_list': Appointment_list, 'manager_user': manager_user,'Appointment_search_list':Appointment_search_list})
   # else:
   return render(request,'manager/appointment.html',{'Appointment_list' : Appointment_list,'manager_user':manager_user})

@login_required(login_url='login')
def ManagePatient(request):
   manager_user = Manager.objects.get(user=request.user)
   Patient_list = Patient.objects.all()     
   return render(request,'manager/patient.html',{'Patient_list' : Patient_list,'manager_user':manager_user})

@login_required(login_url='login')
def ManageUser(request):
   manager_user = Manager.objects.get(user=request.user)
   All_user = User.objects.all()
   return render(request,'manager/user.html',{'manager_user':manager_user,'All_user':All_user})

@login_required(login_url='login')
def ManageDoctor(request):
   manager_user =Manager.objects.get(user=request.user)
   doctors = Doctor.objects.all()
   return render(request,'manager/manage_doctor.html',{'manager_user':manager_user,'doctors':doctors})

@login_required(login_url='login')
def PatientData(request):
   manager_user = Manager.objects.get(user=request.user)
   return render(request,'manager/view_data_patient.html',{'manager_user':manager_user})

@login_required(login_url='login')
def ManageSpecification(request):
   manager_user = Manager.objects.get(user=request.user)
   specification_numberofdoctora = []
   all_specification = Specialization.objects.all()
   for specialization in all_specification:
       number_doctors = Doctor.objects.filter(Specialization=specialization).count()
       specification_numberofdoctora.append((specialization,number_doctors))
   return render(request,'manager/view_data_patient.html',{'manager_user':manager_user,'list_spec_num':specification_numberofdoctora})

@login_required(login_url='login')
def descrption(request,id):
    manager_user = Manager.objects.get(user=request.user)
    # descrption = request.POST['descrption'] 
    #  created_descrption = Appointment.objects.get(id = id)
    # created_descrption.descrption = descrption
    # created_descrption.save() 
    return render(request,'manager/descrption-form-.html',{'descrption_Paragrah' : Patient.objects.get(id = id).descrption,'manager_user':manager_user})
    # return redirect('/Patient/AppointHistory')       
@login_required(login_url='login')
def deleteUser(request,id):
    User.objects.get(id = id).delete()
    return redirect('/Manager/ManageUser')
@login_required(login_url='login')
def deleteDoctor(request,id):
    Doctor.objects.get(id = id).delete()
    return redirect('/Manager/ManageDoctor')

@login_required(login_url='login')
def deleteSpecialization(request,id):
    Specialization.objects.get(id = id).delete()
    return redirect('/Manager/ManageSpecification')
def deleteAppointment(request,id):
    Appointment.objects.get(id = id).delete()
    return redirect('/Manager/Appointment')
@login_required(login_url='login')
def edit_doctor(request,id):
    Doctor_user = Doctor.objects.get(id=id)
    manager_user = Manager.objects.get(user=request.user)
    if request.method == "POST":
        form = ProfileDoctor(request.POST , request.FILES ,  instance = Doctor_user)
        if form.is_valid:
            form.save()
            return redirect('/Manager/ManageDoctor')
    else:
        form = ProfileDoctor(instance = Doctor_user)
    return render(request, 'manager/edit_doctor.html',{'form':form,'Doctor':Doctor_user,'manager_user':manager_user})
@login_required(login_url='login')
def edit_Appointment(request,id):
    appointment = Appointment.objects.get(id=id)
    manager_user = Manager.objects.get(user=request.user)
    form = Appointmentform(instance = appointment)
    return render(request, 'manager/descrption-form.html',{'form':form,'manager_user':manager_user})

@login_required(login_url='login')
def edit_Specialization(request,id):
    specialization = Specialization.objects.get(id=id)
    manager_user = Manager.objects.get(user=request.user)
    if request.method == "POST":
        form = Specializationform(request.POST , request.FILES ,  instance = specialization)
        if form.is_valid():
            form.save()
            return redirect('/Manager/ManageSpecification')
        else:
            return render(request, 'manager/edit_Specialization.html',{'form':form , 'errors': form.errors,'manager_user':manager_user})
            
    else:
        form = Specializationform(instance = specialization)
        return render(request, 'manager/edit_Specialization.html',{'form':form , 'errors': form.errors,'manager_user':manager_user})

@login_required(login_url='login')
def profile(request):
    manager_user= Manager.objects.get(user=request.user)

    if request.method == "POST":
        form = ManagerProfile(request.POST, request.FILES,
                              instance=manager_user)
        if form.is_valid:
            form.save()
            return redirect('Dashboard')
    else:
        form = ManagerProfile(instance=manager_user)
    return render(request, 'manager/manager_profile.html', {'form': form, 'manager_user': manager_user})
