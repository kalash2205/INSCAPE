from django.db import models
from django.contrib.auth.models import User
from staff.models import Specialities
import uuid

# Create your models here.


class Patient(models.Model):
    
    PATIENT_TYPE =(
        ('IPD', 'In patient'),
        ('OPD', 'Out patient'),
    )
    GENDER_TYPE  = (
        ('M', 'male'),
        ('F', 'female'),
        ('O', 'other')
    )
    BLOOD_TYPE=(
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('O+', 'O+'),
        ('AB+', 'AB+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('O-', 'O-'),
        ('AB-', 'AB-'),     
    )   
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    contact = models.IntegerField(null=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    # patient_image = models.ImageField(null=True, blank=True, upload_to = '', default='')
    id = models.AutoField(primary_key=True, editable=False)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length = 200, choices = GENDER_TYPE, null=True)
    arrival = models.DateTimeField(auto_now_add=True)
    blood_group = models.CharField(max_length =200, choices=BLOOD_TYPE, null=True)
    type = models.CharField(max_length =200, choices = PATIENT_TYPE, null=True)
    treatment_category = models.ForeignKey(Specialities, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.username)
    
       
class Tests(models.Model):
    
    # TEST_NAME = (
    #     ('', ''),
    #     ('', ''),
    #     ('', ''),
    #     ('', ''),
    #     ('', ''),
    #     ('', ''),
    #     ('', ''),
    #     ('', ''),
    #     ('', ''),
    #     ('', ''),
    #     ('', ''), 
    # )
    towner= models.ForeignKey(Patient, null=True, blank=True, on_delete=models.CASCADE)
    id=models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)
    tname = models.CharField(max_length=200)
    tcost = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return str(self.tname)
    
       
class Meds(models.Model):
    
    # CATEGORY = (
    #     ('p', 'primary'),
    #     ('m', 'moderate'),
    #     ('a', 'advanced'),         
    # )  
    mowner= models.ForeignKey(Patient, null=True, blank=True, on_delete=models.CASCADE)
    id=models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable=False)
    mname=models.CharField(max_length=200)
    mcost = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return str(self.mname)
    
    # category =  models.CharField(max_length=200, choices = CATEGORY)
    
    
# class Rooms(models.Model):
    
#     # TYPE =(
#     #     ('S', 'single'),
#     #     ('D', 'double'),
#     #     ('M', 'multiple')
#     # )
#     # if Patient.type == 'IPD': 
#     owner = models.ForeignKey(Patient, null=True, blank=True, on_delete=models.CASCADE)
#     id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable=False)
#     rno = models.IntegerField(null=True, blank=True)
#     # type= models.CharField(max_length=200, choices = TYPE)
#     rcost = models.IntegerField(null=True, blank=True)
    
#     def __str__(self):
#         return str(self.rno)
    
    
class Bills(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    bowner = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    bdate = models.DateTimeField(auto_now_add=True)
    btcost= models.ForeignKey(Tests, blank=True, on_delete=models.CASCADE, null=True)
    # brcost= models.ForeignKey(Rooms, blank=True, on_delete=models.CASCADE, null=True)
    bmcost=models.ForeignKey(Meds, blank=True, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.bowner)
    
    

    
    
            
            
    
    
    
  
    
    
    
    
    
    
   
   
    
