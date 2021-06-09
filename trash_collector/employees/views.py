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
    customer_zip = Customer.objects.filter(zip_code=employee.zip_code)
    customer_pickup = customer_zip.filter(pickup_day=today)
    customer_suspend = customer_pickup.filter(suspension_end=None)
    #one time pick up filter
    customer_suspend_2 = customer_zip.filter(suspension_end=None)
    customer_one_pickup = customer_suspend_2.filter(one_time_pickup=datetime.date.today())
    customer_suspend_3 = customer_zip.filter(suspension_end=None)
    context = {
        'customer': customers,
        'employee': employee,
        'customer_zip': customer_zip,
        'customer_pickup': customer_pickup,
        'customer_suspend': customer_suspend,
        'customer_one_pickup': customer_one_pickup,
        'customer_suspend_3': customer_suspend_3
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
    user = request.user
    employee = Employee.objects.get(user=user)
    Customer = apps.get_model('customers.Customer')
    customers = Customer.objects.all()
    now = dt.now()
    today = now.strftime('%A')
    customer_zip = Customer.objects.filter(zip_code=employee.zip_code)
    customer_pickup = customer_zip.filter(pickup_day=today)
    customer_suspend = customer_pickup.filter(suspension_end=None)
    # one time pick up filter
    customer_suspend_2 = customer_zip.filter(suspension_end=None)
    customer_one_pickup = customer_suspend_2.filter(one_time_pickup=datetime.date.today())
    #  Non-suspended account filter
    customer_suspend_3 = customer_zip.filter(suspension_end=None)
    context = {
        'customers': customers,
        'customer_zip': customer_zip,
        'customer_one_pickup': customer_one_pickup,
        'customer_suspend_3': customer_suspend_3
    }
    if request.method == 'POST':
        pickup_day = request.POST.get('pickup_day')
        customer_pickup_filter = customer_zip.filter(pickup_day=pickup_day)
        customer = Customer.objects.get(pickup_day=pickup_day)
        context = {
            'customer': customer,
            'customers': customers,
            'customer_zip': customer_zip,
            'customer_pickup': customer_pickup,
            'customer_suspend': customer_suspend,
            'customer_one_pickup': customer_one_pickup,
            'customer_pickup_filter': customer_pickup_filter,
            'customer_suspend_3': customer_suspend_3
        }
        return render(request, 'employees/index.html', context)
    else:
        return render(request, 'employees/index.html', context)


def confirm(request, customer_id):
    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.get(id=customer_id)
    customer.balance += 19
    customer.completed = None
    customer.save()
    return HttpResponseRedirect(reverse('employees:index'))


def un_confirm(request, customer_id):
    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.get(id=customer_id)
    customer.balance -= 19
    customer.completed = True
    customer.save()
    return HttpResponseRedirect(reverse('employees:index'))
