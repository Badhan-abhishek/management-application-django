from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, PersonForm
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
    # current_user = request.user
    Persons = Person.objects.all()
    context = {'Persons': Persons}
    return render(request, 'manageApp/dashboard.html', context)


@login_required(login_url='login')
def addPerson(request):
    form = PersonForm()
    if request.method=='POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form': form}
    return render(request, 'manageApp/add_person.html', context)

def updatePerson(request, pk):
    person = Person.objects.get(id=pk)
    form = PersonForm(instance=person)
    if request.method=='POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'manageApp/add_person.html', context)

def deletePerson(request, pk):
    person = Person.objects.get(id=pk)
    if request.method == 'POST':
        person.delete()
        return redirect("/")
    context = {'item': person}
    return render(request, 'manageApp/delete.html', context)
    