# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user ,users_list
from django.contrib.auth.views import LogoutView
from django.contrib.auth import get_user_model
User = get_user_model()


urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path('users',users_list,name='users_list'),
]
