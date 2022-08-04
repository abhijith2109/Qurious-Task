from django.contrib import admin
from django.urls import path
from super_admin import views

urlpatterns=[
    path("home",views.SuperAdminHomeView.as_view(),name="home")
]