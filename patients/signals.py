from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Patient
# from django.core.mail import send_mail
from django.conf import settings 



# def spec_id(sender, instance, update_fields=None, **kwargs):
#     if instance.id is None:
#         pass
#     else:

    
    
    
    
    
    
    
# pre_save.connect(spec_id, sender=Patient)    
    
    


def patientcreated(sender, instance, created, **kwargs):
    if created:
        user=instance
        patient=Patient.objects.update_or_create(
            user=user, 
            username=user.username,
            email=user.email,
            name = user.first_name,     
        )
        
        # subject='Welcome to inscape'
        # message = 'We are glad you are here'
        
        # send_mail(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [profile.email]
        # )
        
    print("Patient profile updated")
    
post_save.connect(patientcreated, sender = User)


def updatepatient(sender, instance, created, **kwargs):

    patient=instance
    user = patient.user
    if created == False:
        user.first_name=patient.name
        user.username = patient.username
        user.email = patient.email
        user.save()

post_save.connect(updatepatient, sender=Patient)    
      

# def deletepatient(sender, instance, **kwargs):
#     try:
#         user = instance.user
#         user.delete()
#     except:
#         pass    
#     print("Deleting user") 

# post_delete.connect(deletepatient, sender=Patient) 


# def deleteprofile(sender, instance, **kwargs):
#     user = instance.user
#     user.delete()

# post_delete.connect(deleteprofile, sender=Profile)     
# @receiver(post_save, sender=User)
# @receiver(post_delete, sender=User)
# post_delete.connect(deleteprofile, sender=Profile) 
