from django.shortcuts import render, redirect

# Create your views here.
from users.forms import UserRegistrationForm
from django.views.generic import CreateView, FormView,ListView
from users.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator


class AddUserView(CreateView):
    model = User
    template_name = "adduser.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("home")

class UserListView(ListView):
    model = User
    context_object_name = "users"
    template_name = "user-lists.html"

    def get_queryset(self):
        return User.objects.all()



