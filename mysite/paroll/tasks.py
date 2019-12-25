from __future__ import absolute_import, unicode_literals
from .models import Account
from celery import task
    
@task
def test():
    a = Account(account_type='employee', bank_account='123'
                , address='123', email='jj@jj.com')
    a.using('defaul').save()
    