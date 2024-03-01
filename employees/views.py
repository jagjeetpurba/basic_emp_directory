from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Employees
# Create your views here.
def employee_detail(request,pk):
    employee=get_object_or_404(Employees,pk=pk)
    context={
        'employee':employee
    }
    return render(request,'employee_detail.html',context)