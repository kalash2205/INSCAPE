from django.db import models
from django.contrib.auth.models import User
import uuid
# from django.db.models.expressions import F
# from phonenumber_field.modelfield import PhoneNumberField

# Create your models here.

class Department(models.Model):
    
    # DEPARTMENT=(
    #     ('ADM', 'ADMINISTRATOR'), 
    #     ('MGR', 'MANAGING'), 
    #     ('MTN', 'MAINTENANCE'), 
    #     ('LAB', 'LABORATORY'), 
    #     ('PHR', 'PHARMACY'), 
    #     ('RCP', 'RECEPTION'), 
    #     ('DOC', 'DOCTOR') 
    # )
    
    dname = models.CharField(max_length = 200)     
    dno = models.UUIDField(default = uuid.uuid4, unique = True, primary_key=True, editable=False, null=False)
    # dhead = models.CharField(max_length=200)
    dhead= models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True) 
          
    def __str__(self):
        return str(self.dname)
    
    
# class StaffDepartment(models.Model):
#     dname = models.CharField(max_length=200, null=False)
#     dno = models.UUIDField(primary_key=True, max_length=32, default = uuid.uuid4, unique = True, editable=False)
#     created = models.DateTimeField(auto_now_add=True)
#     dhead = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         # managed = False
#         db_table = 'staff_department'    
            
#     def __str__(self):
#         return str(self.dname)    
    
        

              
    
class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contact = models.IntegerField(null=True)
    address = models.CharField(max_length=500)
    staff_image = models.ImageField(null=True, blank=True, upload_to = 'staffprofiles/', default='staffprofiles/user-default.png')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False, null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE) 
    # department = models.CharField(max_length=200) 
    # intro = models.CharField(max_length=200, null=True, blank=True)
    # about = models.CharField(max_length = 1000, null=True, blank=True)
    # speciality = models.ForeignKey(Specialities, on_delete=models.CASCADE, null=True)
    highest_degree = models.CharField(max_length= 500, null=True, blank=True)
    academics = models.CharField(max_length= 2000, null=True, blank=True)
    certificates = models.CharField(max_length=2000, null=True, blank=True)
    
    # CATEGORY_TYPE = (
    #     ('A', 'admin'),
    #     ('D', 'doctor'),
    #     ('N', 'nurse'),
    #     ('O', 'other'),
    # )
    # salary = models.IntegerField(null=True, blank=True)
    # if dname == 'DOCTOR':  
    # if CATEGORY_TYPE=='D':
    #     post  = models.
    
    @property
    def imageurl(self):
        try:
            url = self.staff_image.url
        except:
            url=''    
        return url        
           
    def __str__(self):
        return str(self.name)
    
    
# class Doctor(models.Model):
#     docname = models.CharField(max_length=200, null=True, blank=True)   
#     def __str__(self):
#         return str(self.name)    
    
    

class Specialities(models.Model):
    sowner = models.ForeignKey(Staff, null=True, blank=True, on_delete=models.CASCADE)
    sname = models.CharField(max_length = 200)    
    sno = models.UUIDField(default = uuid.uuid4, unique = True, primary_key=True, editable=False, null=False)
    created = models.DateTimeField(auto_now_add=True) 
    # overview = models.CharField(max_length=10000000, null=True, blank=True)
    
    
    def __str__(self):
        return str(self.sname)        
    
    
    
    

    
    
    
    
    
    