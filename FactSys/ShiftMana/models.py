from django.db import models


'''
Account class:
    work_state: 'none', 'sick_leave', 'leave', 'CTO', 'BT', 'working'
    work_shift: 'morning', 'evening'
    account_type: 'employee', 'foreman', 'director'
'''
class Account(models.Model):
    identity = models.CharField(max_length=4)
    password = models.CharField(max_length=200, default='00000')
    work_state = models.CharField(max_length=200, default='none') #WT
    work_shift = models.CharField(max_length=200, default='morning') #WS
    work_duration = models.IntegerField(default=0) #in minutes
    account_type = models.CharField(max_length=200)
    #ApplicationState
    

    
    
'''
ApplicationState class:
    state: 'none', 'sick_leave', 'leave', 'CTO', 'approved'
    date:
'''
class ApplicationState(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    state = models.CharField(max_length=200)
    approved = models.BooleanField(default=False)
    date = models.DateField('date applied')
    
    
    
    


class Schedule(models.Model):
    date = models.DateField();
    #ShceduleState




'''
    work_state: 'none', 'sick_leave', 'leave', 'CTO', 'BT', 'working'
    work_shift: 'morning', 'evening'
'''
class ScheduleState(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    identity = models.CharField(max_length=4)
    work_state = models.CharField(max_length=200, default='none') # WT
    work_shift = models.CharField(max_length=200, default='morning') # WS
    
# Create your models here.
