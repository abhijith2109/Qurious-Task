from django.contrib import admin
from django.urls import path,include
from coordinator import views


urlpatterns =[
    path("home",views.CoordinatorHomeView.as_view(),name="coordinator-home"),
    path("login",views.SingnInView.as_view(),name="coordinator-login"),

]