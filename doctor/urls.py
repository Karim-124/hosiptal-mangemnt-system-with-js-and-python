from django.urls import path
from . import views


urlpatterns = [
    path("Dashboard", views.dashboard, name="dr_Dashboard"),
    path("Profile", views.profile, name="dr_Profile"),
    path("myAppointment", views.myAppointment, name="myAppointment"),
    path("patients", views.patientslist, name="patientslist"),
    path('delete/<int:id>', views.deletbook, name='delete'),
    path('descrption_write/<int:id>', views.descrption_write, name='descrption_write'),

]
