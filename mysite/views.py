from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employees

def home(request):
    employee=Employees.objects.all()
    context={
        'employee':employee
    }
    return render(request, 'home.html',context)