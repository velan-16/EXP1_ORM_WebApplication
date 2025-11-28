from django.db import models
from django.contrib import admin

class Employee(models.Model):
    employee_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'email', 'position', 'department')    