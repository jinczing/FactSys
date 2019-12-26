import time
from .models import Account

def update():
    a = Account(identity=str(time.ctime()),
    account_type='employee',bank_account='123',address='123')
    a.save()
    

while True:
    update()
    time.sleep(10)

