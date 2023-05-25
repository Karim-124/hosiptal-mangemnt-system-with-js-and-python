from django.db import models
import uuid
from django.contrib.auth.models import User
from doctor.models import *


# Create your models here.
class Manager(models.Model):
    
    GenderChoices = (
    ('male','male'),
    ('female', 'female'),
)
     
    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    name = models.CharField(max_length=100,blank=True, null=True,default="None")
    email = models.CharField(max_length=100,blank=True, null=True)
    # use default profile image in intial in profile
    profile_img = models.ImageField( upload_to='profile_images',  default='default-profile-image-png-1-Transparent-Images.png')
    phone_number = models.CharField(max_length=20, blank=True, null=True ,default="None")
    address = models.CharField(max_length=100, blank=True, null=True,default="None")
    gender = models.CharField(max_length=6, choices=GenderChoices, blank=True, null=True, default="male")

    def __str__(self):
        return self.user.username

