from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from .models import Employee
from django.urls import reverse
from datetime import datetime as dt
import datetime

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    user = request.user
    employee = Employee.objects.get(user=user)
    Customer = apps.get_model('customers.Customer')
    customers = Customer.objects.all()
    now = dt.now()
    today = now.strftime('%A')
    date = datetime.date.today()
    customer_zip = Customer.objects.filter(zip_code=employee.zip_code)
    customer_pickup = customer_zip.filter(pickup_day=today)
    customer_suspend = customer_pickup.filter(suspension_end=date)
    customer_suspend_2 = customer_zip.filter(suspension_end=date)
    customer_one_pickup = customer_suspend_2.filter(one_time_pickup=date)
    context = {
        'customer': customers,
        'employee': employee,
        'customer_zip': customer_zip,
        'customer_pickup': customer_pickup,
        'customer_suspend': customer_suspend,
        'customer_one_pickup': customer_one_pickup
    }
    return render(request, 'employees/index.html', context)
    # This line will get the Customer model from the other app, it can now be used to query the db


def zip_code(request):
    user = request.user
    if request.method == 'POST':
        employee_zip = Employee.objects.get(user=user)
        employee_zip.zip_code = request.POST.get('zip_code')
        employee_zip.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        employee = Employee.objects.get(user=user)
        context_one = {
            'employee': employee
        }
        return render(request, 'employees/index.html', context_one)


def create(request):
    user = request.user
    new_employee = Employee(name=user.username, user=user)
    new_employee.save()
    return render(request, 'employees/create.html')


def my_view(request):
    Customer = apps.get_model('customers.Customer')
    # customer = Customer.objects.values('zip_code')
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'employees/index.html', context)
