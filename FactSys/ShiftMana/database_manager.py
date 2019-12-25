from .models import Schedule, ScheduleState, Account
from datetime import datetime, timedelta

def shift_map(work_shift, account_type, invert):
    if account_type == 'director':
        return work_shift
    
    if invert == 1:
        if work_shift == 'morning':
            return 'evening'
        else:
            return 'morning'
    else:
        return work_shift


def reset_accounts():
    query = Account.objects.all()
    for account in query:
        account.delete()
    for i in range(1, 24):
        identity = 'A' + str(i).zfill(3)
        if i == 1:
            a = Account(identity=identity, account_type='director', work_shift='morning')
            a.save()
        elif i == 2:
            a = Account(identity=identity, account_type='foreman', work_shift='morning')
            a.save()
        elif i == 3:
            a = Account(identity=identity, account_type='foreman', work_shift='evening')
            a.save()
        elif i > 3 and i < 14:
            a = Account(identity=identity, account_type='employee', work_shift='morning')
            a.save()
        else:
            a = Account(identity=identity, account_type='employee', work_shift='evening')
            a.save()
        

def reset_sd():
    query = Schedule.objects.all()
    for schedule in query:
        schedule.delete()
    query = Account.objects.all()
    
    j = 0
    i = 0
    shift = 0
    while i < 10:
        dt = datetime.now() + timedelta(hours=24*j)
        if dt.weekday() >= 5:
            shift = 1
            j += 1
            continue
        d = dt.date()
        s = Schedule(date=d)
        s.save()
        for account in query:
            s.schedulestate_set.create(identity=account.identity, work_state='none', work_shift=shift_map(account.work_shift, account.account_type, shift)) 
        i += 1
        j += 1
        
    