import datetime

from django.db import models
import datetime
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    pickup_day = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    balance = models.IntegerField(default=0)
<<<<<<< HEAD
=======
    one_time_pickup = models.DateField(default=datetime.date.today())
>>>>>>> 8ea5e7b80ea36c2127703799dfbfa3a03d539343
    suspension_start = models.DateField(default=datetime.date.today())
    suspension_end = models.DateField(default=datetime.date.today())
