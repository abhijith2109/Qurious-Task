from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone=models.CharField(max_length=12)
    profile_pic=models.ImageField(upload_to="images")

    options=(
        ("MANAGER","MANAGER"),
        ("COORDINATOR","COORDINATOR"),
        ("INSPECTOR","INSPECTOR")
    )
    role=models.CharField(max_length=12,choices=options,default="MANAGER")



    @property
    def is_manager(self):
        return self.role=="MANAGER"
    @property
    def is_coordinator(self):
        return self.role=="COORDINATOR"

    @property
    def is_inspector(self):
        return self.role == "INSPECTOR"
