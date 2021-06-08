from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from .models import Employee
from django.urls import reverse

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    user = request.user
    if request.method == 'POST':
        zip_code = request.POST.get('zip_code')
        new_employee = Employee(name=user.username, user=user, zip_code=zip_code)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    # This line will get the Customer model from the other app, it can now be used to query the db
    else:
        # Customer = apps.get_model('customers.Customer')
        # customer = Customer.objects.values('zip_code')
        # context = {
        #     'customer': customer
        # }
        return render(request, 'employees/index.html')

