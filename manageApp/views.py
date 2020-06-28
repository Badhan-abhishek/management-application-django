from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import PersonData, Person
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    return render(request, 'manageApp/home.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard/")
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request, 'manageApp/login.html')


def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        try:
            if form.is_valid:
                form.save()
                messages.success(request, "Account created successfully!")
                return redirect('/auth/login/')
        except ValueError:
            messages.warning(request, "Please recheck credentials")
            return redirect('/auth/register/')
    context = {'form': form}
    return render(request, 'manageApp/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/auth/login/')


@login_required(login_url='login')
def dashboard(request):
    current_user = request.user
    Persons = PersonData.objects.all()
    context = {'Persons': Persons, 'user': current_user}
    return render(request, 'manageApp/dashboard.html', context)
