# views.py
from django.shortcuts import render
from .models import Project, Employee, Task

def dashboard(request):
    projects = Project.objects.all()
    employees = Employee.objects.all()
    tasks = Task.objects.select_related('assigned_to').all()
    context = {
        'projects': projects,
        'employees': employees,
        'tasks': tasks,
    }
    return render(request, 'projects/dashboard.html', context)  # Corrected path here
