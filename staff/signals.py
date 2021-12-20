from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Staff
# from django.core.mail import send_mail
from django.conf import settings 


# def staffcreated(sender, instance, created, **kwargs):
#     if created:
#         user=instance
#         staff=Staff.objects.create(
#             user=user, 
#             username=user.username,
#             email=user.email,
#             name = user.first_name,
#         )
          
#     print("Staff profile updated")
    
# post_save.connect(staffcreated, sender=User)


def updatestaff(sender, instance, created, **kwargs):
    staff=instance
    user = staff.user
    if created == False:
        user.first_name=staff.name
        user.username = staff.username
        user.email = staff.email
        user.save()

post_save.connect(updatestaff, sender=Staff)    
      

def deletestaff(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass    
    print("Deleting user") 

post_delete.connect(deletestaff, sender=Staff) 


# def deleteprofile(sender, instance, **kwargs):
#     user = instance.user
#     user.delete()

# post_delete.connect(deleteprofile, sender=Profile)     
# @receiver(post_save, sender=User)
# @receiver(post_delete, sender=User)
# post_delete.connect(deleteprofile, sender=Profile) 



# def updateuser(sender, instance, created, **kwargs):
#     profile=instance
#     user = profile.user
#     if created == False:
#         user.first_name=profile.name
#         user.username = profile.username
#         user.email = profile.email
#         user.save()

# post_save.connect(updateuser, sender=Profile)    