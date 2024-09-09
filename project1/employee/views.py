from django.shortcuts import render
from employers.models import Employee
# def index(request):
    # return render(request,'index.html')

def homepage(request):
    employees=Employee.objects.all()
    print(employees)
    context={
    'employee':employees,
    }
    return render(request,'index.html',context)