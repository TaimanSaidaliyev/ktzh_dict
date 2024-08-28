from django.shortcuts import render
from .models import *


def home_view(request):
    employees = Employee.objects.filter(fired=False)
    department = Department.objects.all()
    division = Division.objects.all()

    context = {
        'employees': employees,
        'department': department,
        'division': division
    }

    return render(request, 'employees/home.html', context)


def employee_profile(request, id):
    employee = Employee.objects.get(id=id)
    context = {
        'employee': employee
    }

    return render(request, 'employees/employee.html', context)