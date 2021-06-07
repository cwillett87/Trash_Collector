from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    print(user)
    return render(request, 'customers/index.html')


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user = request.user
        pickup_day = request.POST.get('pickup_day')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        new_customer = Customer(name=name, user=user,  pickup_day=pickup_day, address=address, zip_code=zip_code)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:details'))
    else:
        return render(request, 'customers/create.html')


def details(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    context = {
        'customer': customer
    }
    return render(request, 'customers/details.html', context)


def edit(request):
    if request.method == 'POST':
        user = request.user
        customer_edit = Customer.objects.get(user=user)
        customer_edit.name = request.POST.get('name')
        customer_edit.pickup_day = request.POST.get('pickup_day')
        customer_edit.address = request.POST.get('address')
        customer_edit.zip_code = request.POST.get('zip_code')
        customer_edit.save()
        return HttpResponseRedirect(reverse('customers:details'))
    else:
        user = request.user
        customer_edit = Customer.objects.get(user=user)
        context = {
            'customer': customer_edit
        }
        return render(request, 'customers/edit.html', context)


def suspend(request):
    if request.method == 'POST':
        user = request.user
        customer_suspend = Customer.objects.get(user=user)
        customer_suspend.suspension_start = request.POST.get('suspension_start')
        customer_suspend.suspension_end = request.POST.get('suspension_end')
        customer_suspend.save()
        return HttpResponseRedirect(reverse('customers:details'))
    else:
        user = request.user
        customer_suspend_date = Customer.objects.get(user=user)
        context = {
            'customer': customer_suspend_date
        }
        return render(request, 'customers/suspend.html', context)


# def activate(request):
#     user = request.user
#     customer_activate = Customer.objects.get(user=user)
#     context = {
#         'customer': customer_activate
#     }
#     if request.method == 'POST':
#         customer_activate.suspension_start.delete()
#         customer_activate.suspension_end.delete()
#         return HttpResponseRedirect(reverse('customers:details'))
#     else:
#         return render(request, 'customers/activate.html', context)
