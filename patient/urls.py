from django.urls import path
from . import views

urlpatterns = [
    path("Dashboard", views.dashboard, name="Dashboard"),
    path("Profile", views.profile, name="Profile"),
    path("BookAppointment_1", views.bookAppointment_1, name="BookAppointment_1"),
    path("BookAppointment_2/<slug>/", views.bookAppointment_2, name="BookAppointment_2"),
    path("AppointHistory", views.appointHistory, name="AppointHistory"),
    path('delete/<int:id>', views.deletbook, name='delete'),
    path('descrption/<int:id>', views.descrption, name='descrption'),
]
