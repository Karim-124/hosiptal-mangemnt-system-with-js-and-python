from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # Create your views here.
from .models import *
from doctor.models import *
import datetime
from .forms import *
from django.contrib.auth.decorators import login_required
Date = None
speciality = None


@login_required(login_url='login')
def dashboard(request):
    patient_user = Patient.objects.get(user=request.user)
    return render(request, 'patient_dashbord.html', {'patient': patient_user})


@login_required(login_url='login')
def profile(request):
    object_Patient = Patient.objects.get(user=request.user)

    if request.method == "POST":
        form = ProfilePatient(request.POST, request.FILES,
                              instance=object_Patient)
        if form.is_valid:
            form.save()
            return redirect('/Patient/Dashboard')
    else:
        form = ProfilePatient(instance=object_Patient)
    return render(request, 'dashbord-profile.html', {'form': form, 'patient': object_Patient})


@login_required(login_url='login')
def bookAppointment_1(request):
    patient_user = Patient.objects.get(user=request.user)
    specialization_doctor = Specialization.objects.all()
    if request.method == "POST":
        Date = request.POST.get('Date')
        speciality = request.POST.get('speciality')
        check = datetime.datetime.strptime(
            Date + " 08:15:27.243860", '%Y-%m-%d %H:%M:%S.%f').date() < datetime.datetime.now().date()
        if check:
            return render(request, 'dashbord-form1book.html', {'patient': patient_user, 'specialization_doctor': specialization_doctor,  'check': check})
        else:
            return redirect('BookAppointment_2', slug=str(str(Date)+"_"+str(speciality)))

    return render(request, 'dashbord-form1book.html', {'patient': patient_user, 'specialization_doctor': specialization_doctor, 'check': False, })


@login_required(login_url='login')
def bookAppointment_2(request, slug):
    patient_user = Patient.objects.get(user=request.user)
    slug = str(slug)
    Date = str(slug[0: slug.index('_')])
    speciality = str(slug[slug.index('_') + 1:])
    list_available_dates = []
    print(speciality)
    id = Specialization.objects.get(name=speciality)
    list_of_doctor = Doctor.objects.all().filter(Specialization=id)
    for doctor in list_of_doctor:
        free_time = docter_schedule.objects.filter(
            Date_Book=Date, doctor=doctor).first()

        if free_time == None:
            free_time = docter_schedule.objects.create(
                Date_Book=Date, doctor=doctor)
            free_time.save()
        if free_time.data1 == False:
            list_available_dates.append(free_time)
        elif free_time.data2 == False:
            list_available_dates.append(free_time)
        elif free_time.data3 == False:
            list_available_dates.append(free_time)
        elif free_time.data4 == False:
            list_available_dates.append(free_time)
        elif free_time.data5 == False:
            list_available_dates.append(free_time)

    if request.method == "POST":
        Id = request.POST.get('ScheduleID')
        user_phone_number = request.POST.get('user_phone_number')
        name_order = request.POST.get('user_name')
        selected_schedule = docter_schedule.objects.get(id=Id)
        selected_doctor = selected_schedule.doctor
        str_selected_schedule = str(selected_schedule)
        Date_Appointment = str_selected_schedule[str_selected_schedule.index(
            'y ')+1:]
        # update selected_schedule
        if selected_schedule.data1 == False:
            selected_schedule.data1 = True
        elif selected_schedule.data2 == False:
            selected_schedule.data2 = True
        elif selected_schedule.data3 == False:
            selected_schedule.data3 = True
        elif selected_schedule.data4 == False:
            selected_schedule.data4 = True
        elif selected_schedule.data5 == False:
            selected_schedule.data5 = True
        elif selected_schedule.data6 == False:
            selected_schedule.data6 = True

        selected_schedule.save()
        # create Appointment
        Appointment.objects.create(patient=patient_user, doctor=selected_doctor, name=name_order,
                                   phone_number=user_phone_number, data_time=Date_Appointment).save()
        # update list_available_dates
        list_available_dates = []
        for doctor in list_of_doctor:
            free_time = docter_schedule.objects.filter(
                Date_Book=Date, doctor=doctor).first()

            if free_time == None:
                free_time = docter_schedule.objects.create(
                    Date_Book=Date, doctor=doctor)
                free_time.save()
            if free_time.data1 == False:
                list_available_dates.append(free_time)
            elif free_time.data2 == False:
                list_available_dates.append(free_time)
            elif free_time.data3 == False:
                list_available_dates.append(free_time)
            elif free_time.data4 == False:
                list_available_dates.append(free_time)
            elif free_time.data5 == False:
                list_available_dates.append(free_time)

        return redirect('/Patient/Dashboard')
    else:
        return render(request, 'dashbord-form2book.html', {'patient': patient_user, 'list_available_dates': list_available_dates})


@login_required(login_url='login')
def appointHistory(request):
    patient_user = Patient.objects.get(user=request.user)
    patient_Appointment = Appointment.objects.all().filter(patient=patient_user)
    return render(request, 'dashbord-AppointHistory.html', {'patient': patient_user, 'Data_Appointment': patient_Appointment})


@login_required(login_url='login')
def deletbook(request, id):
    Appointment.objects.get(id=id).delete()
    return redirect('/Patient/AppointHistory')


@login_required(login_url='login')
def descrption(request, id):
    patient_user = Patient.objects.get(user=request.user)
    return render(request, 'descrption-form-.html', {'patient': patient_user, 'descrption_Paragrah': Appointment.objects.get(id=id).descrption})
