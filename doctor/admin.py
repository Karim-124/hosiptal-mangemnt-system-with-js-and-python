from django.contrib import admin
from .models import Doctor,Specialization,docter_schedule,Appointment

admin.site.register(Doctor)
admin.site.register(Specialization)
admin.site.register(docter_schedule)
admin.site.register(Appointment)
