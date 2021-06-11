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
    print(user)
    return render(request, 'employees/index.html')

    # This line will get the Customer model from the other app, it can now be used to query the db


def zip_code(request):
    user = request.user
    if request.method == 'POST':
        employee_zip = Employee.objects.get(user=user)
        employee_zip.name = request.POST.get('name')
        employee_zip.zip_code = request.POST.get('zip_code')
        employee_zip.save()
        return HttpResponseRedirect(reverse('employees:my_view'))
    else:
        employee = Employee.objects.get(user=user)
        context_one = {
            'employee': employee
        }
        return render(request, 'employees/zip_code.html', context_one)


def create(request):
    user = request.user
    if request.method == 'POST':
        new_employee = Employee(user=user)
        new_employee.name = request.POST.get('name')
        new_employee.zip_code = request.POST.get('zip_code')
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:my_view'))
    else:
        employee = Employee.objects.get(user=user)
        context = {
            'employee': employee
        }
        return render(request, 'employees/create.html', context)


def my_view(request):
    user = request.user
    employee = Employee.objects.get(user=user)
    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.all()
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
        'customer': customer,
        'employee': employee,
        'customer_zip': customer_zip,
        'customer_pickup': customer_pickup,
        'customer_one_pickup': customer_one_pickup,
        'customer_suspend': customer_suspend,
        'customer_suspend_3': customer_suspend_3
    }
    if request.method == 'POST':
        pickup_day = request.POST.get('pickup_day')
        customer_pickup_filter = customer_zip.filter(pickup_day=pickup_day)
        context = {
            'pickup_day': pickup_day,
            'employee': employee,
            'customer': customer,
            'customer_zip': customer_zip,
            'customer_pickup': customer_pickup,
            'customer_suspend': customer_suspend,
            'customer_one_pickup': customer_one_pickup,
            'customer_pickup_filter': customer_pickup_filter,
            'customer_suspend_3': customer_suspend_3
        }
        return render(request, 'employees/my_view.html', context)
    else:
        return render(request, 'employees/my_view.html', context)


def confirm(request, customer_id):
    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.get(id=customer_id)
    customer.balance += 19
    customer.completed = None
    customer.save()
    return HttpResponseRedirect(reverse('employees:my_view'))


def un_confirm(request, customer_id):
    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.get(id=customer_id)
    customer.balance -= 19
    customer.completed = True
    customer.save()
    return HttpResponseRedirect(reverse('employees:my_view'))
