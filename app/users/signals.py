#SIGNALS
import profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile



#using decorators to signals

#Automatically create a Profile when a user is created
@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )

#update user credentials when a profile was updated
@receiver(post_save, sender=Profile)
def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False: #check if user doesnt exist
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()
    


#When a profile is deleted, user also is deleted
#to avoid orphans data
@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    
# Connecting signals without using decorators
# post_save.connect(profileUpdated, sender=Profile)
# post_delete.connect(deleteUser, sender=Profile)