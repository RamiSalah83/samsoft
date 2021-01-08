# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db.models.signals import post_save
from novav1.models import  Branch , DoctorIn

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            section_name = form.cleaned_data.get("section_name")
            branch = form.cleaned_data.get("branch")
            user = authenticate(username=username, password=raw_password ,section_name=section_name, branch=branch)
            print(user.section_name_id)
            if  user.section_name_id == 4 :
                obj = DoctorIn.objects.create(
                        id=user.pk,
                        DocName=username,
                ) 
            msg     = 'User created - please <a href="/login">login</a>.'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })



def  users_list(request):
    users_list= User.objects.all()
    context={

        'users_list':users_list
    }


    return render(request,'authentication/templates/users_list.html',context)