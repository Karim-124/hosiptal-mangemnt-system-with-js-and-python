from django.urls import path
from . import views

urlpatterns = [
    path("Dashboard", views.Dashboard, name="Dashboard"),
    path("AddDoctor", views.AddDoctor, name="AddDoctor"),
    path("Appointment", views.myAppointment, name="myAppointment"),
    path("AddSpecification", views.AddSpecification, name="AddSpecification"),
    path("AddUser", views.AddUser, name="AddUser"),
    path("ManagePatient", views.ManagePatient, name="ManagePatient"),
    path("ManageUser", views.ManageUser, name="ManageUser"),
    path("ManageDoctor", views.ManageDoctor, name="ManageDoctor"),
    path("ManageSpecification", views.ManageSpecification, name="ManageSpecification"),
    # path('delete/<int:id>', views.deletbook, name='delete'),
    path('descrption/<int:id>', views.descrption, name='descrption'),
    path('deleteUser/<int:id>', views.deleteUser, name='deleteUser'),
    path('deleteDoctor/<int:id>', views.deleteDoctor, name='deleteDoctor'),
    path('deleteAppointment/<int:id>', views.deleteAppointment, name='deleteAppointment'),
    path('deleteSpecialization/<int:id>', views.deleteSpecialization, name='deleteSpecialization'),
    path('edit_doctor/<int:id>', views.edit_doctor, name='edit_doctor'),
    path('edit_Specialization/<int:id>', views.edit_Specialization, name='edit_Specialization'),
    path('descrption-form/<int:id>', views.edit_Appointment, name='edit_Appointment'),
    path('ManagerProfile', views.profile, name='profile'),
]
