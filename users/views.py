from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterFormAdmin, UserRegisterFormInnovator
from django.contrib import messages
from .models import Profile
from .forms import UserUpdationForm
from django.contrib.auth.models import User


# Create your views here.

# Registration for Admin Users
def AdminUserRegisteration(request):
    form = UserRegisterFormAdmin()
    if request.method == 'POST':
        form = UserRegisterFormAdmin(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user-login')
        else:
            print(form.errors)

    context = {
        'form': form
    }
    return render(request, template_name='users/createUser.html', context=context)


# Registrationn for Innovators
def InnovatorUserRegisteration(request):
    form = UserRegisterFormInnovator()
    if request.method == 'POST':
        form = UserRegisterFormAdmin(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user-login')
        else:
            print(form.errors)

    context = {
        'form': form
    }
    return render(request, template_name='users/CreateInnovatorUser.html', context=context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('challenge-list')
        else:
            messages.error(request, 'Username or password is incorrect...')
            return render(request, template_name='users/UserLogin.html')

    return render(request, template_name='users/UserLogin.html')


def logoutuser(request):
    logout(request)
    return render(request, template_name='challenges/Home.html')


def myprofile(request):
    instance = request.user.profile
    form = UserUpdationForm(instance=instance)
    form.instance.user = request.user
    form.instance.email = request.user.email
    if request.method == 'POST':
        print('profile post request <------')
        form = UserUpdationForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, template_name='users/MyProfile.html', context=context)
