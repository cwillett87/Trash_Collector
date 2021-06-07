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
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create.html')


def details(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    context = {
        'customer': customer
    }
    return render(request, 'customers/details.html', context)
