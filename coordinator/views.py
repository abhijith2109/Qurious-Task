from django.shortcuts import render, redirect

# Create your views here.
from users.forms import UserRegistrationForm, LoginForm
from django.views.generic import CreateView, FormView,TemplateView
from users.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator

class CoordinatorHomeView(TemplateView):
    template_name = "coordinator-home.html"

class SingnInView(FormView):
    model = User
    form_class = LoginForm
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if not user:
                return render(request, "login.html", {"form": form})
            login(request, user)
            if request.user.is_coordinator:
                return redirect("coordinator-home")
            elif request.user.is_manager:
                pass
            else:
                return redirect("index")
