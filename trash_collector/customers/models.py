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
    one_time_pickup = models.DateField(blank=True, null=True)
    suspension_start = models.DateField(blank=True, null=True)
    suspension_end = models.DateField(blank=True, null=True)

    def activate(self):
        if self.suspension_end is None:
            return True
        else:
            return False

    def pickup(self):
        if self.one_time_pickup is None:
            return True
        else:
            return False
