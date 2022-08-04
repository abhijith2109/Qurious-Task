from django.shortcuts import render

# Create your views here.
from users.forms import UserRegistrationForm
from django.views.generic import CreateView, FormView,TemplateView
from users.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout


class SuperAdminHomeView(TemplateView):
    template_name = "superadmin-home.html"


class HomeView(TemplateView):
    template_name = "home.html"
