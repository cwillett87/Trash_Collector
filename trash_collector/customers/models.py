from django.db import models
import datetime
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    balance = models.IntegerField(default=0)
    suspension_start = models.DateField(default=datetime.date.today())
    suspension_end = models.DateField(default=datetime.date.today())
