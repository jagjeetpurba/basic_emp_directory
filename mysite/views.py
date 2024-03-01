from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employees

def index(request):
    employee=Employees.objects.all()
    context={
        'employee':employee
    }
    return render(request, 'index.html',context)