from django.contrib import admin
from django.urls import path
from users import views

urlpatterns=[
    path("add",views.AddUserView.as_view(),name="adduser"),
    path("list",views.UserListView.as_view(),name="userlists"),

]