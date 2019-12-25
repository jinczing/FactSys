from django.db import models


'''
Account class:
    account_type: 'employee', 'foreman', 'director'
'''
class Account(models.Model):
    identity = models.CharField(max_length=4,default='0000')
    password = models.CharField(max_length=200, default='00000')
    account_type = models.CharField(max_length=200)
    bank_account = models.CharField(max_length=200)
    address = models.CharField(max_length=200000)
    email = models.EmailField(default = 'none')
    approved = models.IntegerField(default=0)
    #ApplicationState

class paycheck(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    identity = models.CharField(max_length=4,default=0000)
    work_hour = models.IntegerField(default=0)
    deduction = models.CharField(max_length=200000)
    salary = models.CharField(max_length=2000000)
# Create your models here.
