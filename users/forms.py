from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterFormAdmin(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_staff']
        labels = {
            'is_staff': 'Hoster Access( This enables the permission to  host and run hackathons )'
        }


class UserRegisterFormInnovator(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
