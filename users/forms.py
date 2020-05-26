from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms.models import ModelForm


class UserRegisterFormAdmin(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_staff']
        labels = {
            'is_staff': 'Hoster Access( This enables the permission to  host Hackathons and Review Submissions )'
        }


class UserRegisterFormInnovator(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'bio', 'profile_pic', ]

    def __init__(self, *args, **kwargs):
        super(UserUpdationForm, self).__init__(*args, **kwargs)
