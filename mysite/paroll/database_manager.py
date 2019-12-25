from django.db import models
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.join('../'), 'FactSys')))
import ShiftMana.models
from ShiftMana.models import Account as Account2
from .models import Account



def test():
    return Account2.objects.using('shift_mana').all()
