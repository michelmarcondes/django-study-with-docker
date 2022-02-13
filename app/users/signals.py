# SIGNALS
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

# for email use
from django.core.mail import send_mail
from django.conf import settings


# using decorators to signals

# Automatically create a Profile when a user is created
@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

        # send welcome email
        subject = 'Welcome to DevSearch Django Project'
        message = '''Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators. 
                    To achieve this, it would be necessary to have uniform grammar, pronunciation and more common words.

                    If several languages coalesce, the grammar of the resulting language is more simple and regular than 
                    that of the individual languages. The new common language will be more simple and regular than the 
                    existing European languages. It will be as simple as Occidental; in fact, it will be Occidental.'''

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )


# update user credentials when a profile was updated
@receiver(post_save, sender=Profile)
def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:  # check if user doesnt exist
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


# When a profile is deleted, user also is deleted
# to avoid orphans data
@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

# Connecting signals without using decorators
# post_save.connect(profileUpdated, sender=Profile)
# post_delete.connect(deleteUser, sender=Profile)
