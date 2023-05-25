from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from patient.models import *


class Specialization(models.Model):

    name = models.CharField(max_length=100,  blank=True, null=True,unique=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    GenderChoices = (
        ('male', 'male'),
        ('female', 'female'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    Specialization = models.ForeignKey(
        Specialization, on_delete=models.CASCADE, null=True)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    profile_img = models.ImageField(
        upload_to='profile_images', default='default-profile-image-png-1-Transparent-Images.png')
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(
        max_length=100, blank=True, null=True, default="None")
    salary = models.IntegerField(default=250)
    address = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(
        max_length=6, choices=GenderChoices, blank=True, null=True, default="male")

    def __str__(self):
        return self.user.username


class docter_schedule(models.Model):

    Date_Book = models.DateField(blank=True, null=True)
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, blank=True, null=True)
    data1 = models.BooleanField(default=False)
    data2 = models.BooleanField(default=False)
    data3 = models.BooleanField(default=False)
    data4 = models.BooleanField(default=False)
    data5 = models.BooleanField(default=False)
    data6 = models.BooleanField(default=False)

    def __str__(self):
        if self.data1 == False:
            x = 'Dr.' + str(self.doctor.user) + ' at day ' + str(self.Date_Book) + ' form ' + str("08 to 10 AM")
        elif self.data2 == False:
            x = 'Dr.' + str(self.doctor.user) + ' at day ' + str(self.Date_Book) + ' form ' + str("10 to 12 PM")
        elif self.data3 == False:
            x = 'Dr.' + str(self.doctor.user) + ' at day ' + str(self.Date_Book) + ' form ' + str("12 to 01 PM")
        elif self.data4 == False:
            x = 'Dr.' + str(self.doctor.user) + ' at day ' + str(self.Date_Book) + ' form ' + str("01 to 02 PM")
        elif self.data5 == False:
            x = 'Dr.' + str(self.doctor.user) + ' at day ' + str(self.Date_Book) + ' form ' + str("02 to 04 PM")
        elif self.data6 == False:
            x = 'Dr.' + str(self.doctor.user) + ' at day ' + str(self.Date_Book) + ' form ' + str("04 to 06 PM")
        else:
            x = 'Dr.' + str(self.doctor.user) + ' at day ' + str(self.Date_Book) + ' is ' + str("Full")
        return x

    # def save(self, *args, **kwargs):
    #     super(Doctor, self).save(*args, **kwargs)
    # def create_Doctor(sender, **kwargs):
    #     if kwargs['created']:
    #         print(type(kwargs['instance']))
    #         Doctor.objects.create(user=kwargs['instance'])
    #
    # post_save.connect(create_Doctor, sender=User)
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    patient = models.ForeignKey( Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey( Doctor, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    data_time = models.CharField(max_length=100)
    descrption = models.TextField(max_length=500, blank=True, null=True,default="None")
    def __str__(self):
        return str(self.patient)+" have appointment with Dr."+str(self.doctor)