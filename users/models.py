from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#
# USER_TYPE = (
#     ('HOSTER', 'HOSTER'),
#     ('INNOVATOR', 'INNOVATOR'),
#     ('REVIEWER', 'REVIEWER'),
# )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user_type = models.CharField(choices=USER_TYPE, max_length=10, null=True)
    profile_pic = models.ImageField(default='default.png', upload_to='profile_pics')
    email = models.EmailField(null=True)
    bio = models.TextField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.user.username
