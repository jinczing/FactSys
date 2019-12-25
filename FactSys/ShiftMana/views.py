from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Account, Schedule
from datetime import datetime
import re

token = ''

def auth_table(auth_str):
    if auth_str == 'employee':
        return 1
    if auth_str == 'foreman':
        return 2
    if auth_str == 'director':
        return 3


def index(request):
    return HttpResponse('hello, world.')



def login(request):
    global token
    token = ''
    return render(request, 'ShiftMana/login.html')


def apply(request):
    global token
    if token == '':
        return render(request, 'ShiftMana/error.html', {'message':'please login!'})
    return render(request, 'ShiftMana/apply.html')


def approve(request):
    global token
    if token == '':
        return render(request, 'ShiftMana/error.html', {'message':'please login!'})
    else:
        accounts = []
        auth_level = auth_table(Account.objects.get(identity=token).account_type)
        if auth_level == 2:
            query = Account.objects.exclude(account_type='director')
            for account in query:
                if account.identity == token:
                    continue
                accounts.append(account)
        else:
            query = Account.objects.all()
            for account in query:
                if account.identity == token:
                    continue
                accounts.append(account)
                
        return render(request, 'ShiftMana/approve.html', {'accounts':accounts})


def transfer(request, trans_type):
    global token
    if trans_type == 'login':
        try:
            account = Account.objects.get(identity=request.POST['identity'])
        except (KeyError, Account.DoesNotExist):
            return render(request, 'ShiftMana/error.html', {'message':'ID or password is wrong!'})
        else:
            if account.password != request.POST['password']:
                return render(request, 'ShiftMana/error.html', {'message':'ID or password is wrong!'})
            token = account.identity
            return HttpResponseRedirect(reverse('main'))
        
    if trans_type == 'account_manage':
        if token == '':
            return render(request, 'ShiftMana/error.html', {'message':'please login!'}) 
        else:
            auth_level = auth_table(Account.objects.get(identity=token).account_type)
            if auth_level == 2:
                query = Account.objects.exclude(account_type='director')
                i = 1
                for account in query:
                    if account.identity == token:
                        continue
                    if request.POST['del'+str(i)] == 'true':
                        account.delete()
                        i += 1;
                        continue
                    account.account_type = request.POST['auth'+str(i)];
                    account.save()
                    i += 1;
            if auth_level == 3:
                query = Account.objects.all()
                i = 1
                for account in query:
                    if account.identity == token:
                        continue
                    if request.POST['del'+str(i)] == 'true':
                        account.delete()
                        i += 1
                        continue
                    account.account_type = request.POST['auth'+str(i)];
                    account.save()
                    i += 1;
            return HttpResponseRedirect(reverse('main'))
        
    if trans_type == 'add_account':
        if token == '':
            return render(request, 'ShiftMana/error.html', {'message':'please login!'}) 
        else:
            aID = re.search(r'\b[A-Z][0-9]{3}\b', request.POST['identity'])
            if aID == None or aID.endpos>4:
                return render(request, 'ShiftMana/error.html',
                              {'message':'wrong ID format!'})
            
            if request.POST['identity'][0:aID.endpos] == token:
                return render(request, 'ShiftMana/error.html',
                              {'message':'ID is same as yours!'})
                
            account = Account(identity=request.POST['identity'],
                              account_type=request.POST['type'])
           
            account.save()
            return HttpResponseRedirect(reverse('main'))
        
        
    if trans_type == 'apply_leaving':
        if token == '':
            return render(request, 'ShiftMana/error.html', {'message':'please login!'}) 
        else:
            try:
                s = Schedule.objects.get(date=request.POST['date'])
            except Schedule.DoesNotExist:
                return HttpResponseRedirect(reverse('main'))
            
            account = Account.objects.get(identity=token)
            account.applicationstate_set.create(state=request.POST['type'],
                                                date=request.POST['date'])
            
            
            return HttpResponseRedirect(reverse('main'))
        
    
    if trans_type == 'approve':
        if token == '':
            return render(request, 'ShiftMana/error.html', {'message':'please login!'})
        else:
            auth_level = auth_table(Account.objects.get(identity=token).account_type)
            if auth_level == 2:
                query = Account.objects.exclude(account_type='director')
            else:
                query = Account.objects.all()
            i=1
            for account in query:
                if account.identity == token:
                    continue
                j=1
                for ap in account.applicationstate_set.all():
                    txt = 'approve' + str(i) + '_' + str(j)
                    if ap.approved == False and request.POST[txt] == 'approve':
                        ap.approved = True
                        ap.save()
                        s = Schedule.objects.get(date=ap.date)
                        ss = s.schedulestate_set.get(identity=account.identity)
                        ss.work_state=ap.state
                        ss.save()
                    j += 1
                i += 1
            return HttpResponseRedirect(reverse('main'))
                    
                
            


def main(request):
    global token
    if token == '':
        return render(request, 'ShiftMana/error.html', {'message':'please login!'})
    auth_level = auth_table(Account.objects.get(identity=token).account_type)
    return render(request, 'ShiftMana/main.html', {'identity': token, 
                                                   'auth_level': auth_level})



def schedule(request):
        
    global token
    if token=='':
        return render(request, 'Shiftmana/error.html', {'message':'please login!'})
    else:
        account = Account.objects.get(identity=token)
        account_type = account.account_type
        dates = []
        n_time = datetime.now()
        s = Schedule.objects.filter(date=n_time.date())
        for ss in s:
            dates.append(ss)
        if account_type!='employee':
            for i in range(0, 11):
                n_time += timedelta(hours=24)
                s = Schedule.objects.filter(date=n_time.date())
                for ss in s:
                    dates.append(ss)
        return render(request, 'ShiftMana/schedule.html', {'dates': dates})
    


def account_manage(request):
    global token
    if token == '':
        return render(request, 'ShiftMana/error.html', {'message': 'please login!'})
    else:
        accounts = []
        auth_level = auth_table(Account.objects.get(identity=token).account_type)
        if auth_level == 2:
            query = Account.objects.exclude(account_type='director')
            for account in query:
                if account.identity == token:
                    continue
                accounts.append(account)
        elif auth_level == 3:
            query = Account.objects.all()
            for account in query:
                if account.identity == token:
                    continue
                accounts.append(account)
        return render(request, 'ShiftMana/account_manage.html', {'accounts': accounts, 'auth_level': auth_level})
            