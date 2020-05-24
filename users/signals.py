from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile


def userProfileCreation(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print(f'profile has created for {instance.username}')

    else:
        print('userProfileCreation has broken...')


post_save.connect(userProfileCreation, sender=User)
