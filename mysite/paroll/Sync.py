from django.db import models
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.join('../'), 'FactSys')))
import ShiftMana.models
from ShiftMana.models import Account as Account2
from .models import Account
import time

def force_sync():
    q = Account.objects.all()
    for a in q:
        a.delete()
    q = Account2.objects.using('shift_mana').all()
    for a in q:
        na = Account(identity=a.identity, password=a.password,
        account_type=a.account_type, bank_account='none', address='none')
        na.save()
        
def periodic_sync():
    while True:
        q = Account2.objects.using('shift_mana').all()
        qq = Account.objects.all()
        id_table = []
        for a in q:
            try:
                account = Account.objects.get(identity=a.identity)
            except Account.DoesNotExist:
                account = Account(identity=a.identity, password=a.password,
                account_type=a.account_type, bank_account='none', address='none')
                account.save()
            id_table.append(a.identity)
            account.password = a.password
            account.account_type=a.account_type
            pc = account.paycheck_set.all()
            hour = a.work_duration // 60
            if not pc:
                account.paycheck_set.create(identity=account.identity,
                work_hour=int(hour))
            else:
                pc[0].work_hour = hour
                pc[0].save()
            account.save()
            
        for a in qq:
            if a.identity not in id_table:
                a.delete()
            
        time.sleep(10)
        
