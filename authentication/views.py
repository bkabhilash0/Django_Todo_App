from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.conf import settings


# Create your views here.

def register(request: HttpRequest):
    if request.method == 'GET':
        return render(request, "authentication/register.html")
    if request.method == 'POST':
        fname = request.POST.get("first_name", None)
        lname = request.POST.get('last_name', None)
        uname = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        print(uname)
        errors = []
        if len(fname) <= 5:
            errors.append("First Name must have a minimum of 5 Characters")
        if len(lname) <= 1:
            errors.append("Last Name must have a minimum of 2 Characters")
        if len(uname) <= 6:
            errors.append("User Name must have a minimum of 6 Characters")
        if len(password) <= 8:
            errors.append("Password must have a minimum of 8 Characters")
        try:
            if len(errors) != 0:
                print("ERROR")
                raise Exception("All the Field are Required")
            user, is_new = User.objects.get_or_create(username=uname)
            if not is_new:
                raise Exception("An user with the Username Already Exists!")
            user.first_name = fname
            user.last_name = lname
            user.set_password(password)
            user.email = email
            user.save()
            messages.success(request, "User Created Successfully!")
            return HttpResponseRedirect(reverse("authentication:login"))
        except MultiValueDictKeyError as e:
            messages.add_message(request, messages.ERROR, e)
            return render(request, "authentication/register.html")
        except Exception as e:
            for error in errors:
                messages.error(request, error)
            messages.error(request, "Error Creating User ")
            messages.error(request, e)
            return render(request, "authentication/register.html")


def loginUser(request: HttpRequest):
    if request.method == 'GET':
        return render(request, "authentication/login.html")
    if request.method == 'POST':
        try:
            uname = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=uname, password=password)
            if user is not None:
                messages.success(request, "User Logged in Successfully!")
                login(request, user)
                redirect_url = request.GET.get('next', '/')
                print(redirect_url)
                return redirect(redirect_url)
            else:
                raise Exception("Invalid Credentials")
        except Exception as e:
            messages.error(request, e)
            return render(request, "authentication/login.html")


def logoutUser(request: HttpRequest):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "User Logged Out Successfully!")
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)
    else:
        return render(request, "authentication/login.html")
