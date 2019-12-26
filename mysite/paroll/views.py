from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,FileResponse
from django.urls import reverse
from .models import Account,paycheck
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import io

token =''

def login(request):
    global token
    token = ''
    return render(request, 'paroll/login.html')
    
def transfer(request, trans_type):
    global token
    if trans_type == 'login':
        try:
            account = Account.objects.get(identity=request.POST['identity'])
        except (KeyError, Account.DoesNotExist):
            return render(request, 'paroll/error.html', {'message':'ID or password is wrong!', 'type':0})
        else:
            if account.password != request.POST['password']:
                return render(request, 'paroll/error.html', {'message':'ID or password is wrong!', 'type':0})
            token = account.identity
            return HttpResponseRedirect(reverse('main'))

def main(request):
    level = Account.objects.get(identity = token).account_type
    if level == 'employee':
        level = 1
    elif level == 'fiance':
        level = 2
    else:
        level = 3
    return render(request,"paroll/main.html",{'identity':token,'level':level})


def input_data(request):
    account = Account.objects.all()
    return render(request,"paroll/changedata.html",{'accounts':account}) #return account
                        #3 space to input email,bank accout and address
def show_paycheck(request):
    level = Account.objects.get(identity = token).account_type
    alls = []
    if level == 'employee':
        account = Account.objects.get(identity = token)
        alls = account.paycheck_set.all()
    else:
        alls = paycheck.objects.all()
    return render(request,"paroll/showpaycheck.html",{'temp':alls})

def report(request):
    pass

def approvement(request):
    return render(request,"paroll/approvement.html")     #return alls
                            #one bottom after all account showed
def check(request):
    temp=request.POST['toke']
    if temp == 'one': #one by one
        account = Account.objects.all()
        return render(request,"paroll/approvement_one.html",{'accounts':account})     #return alls
                            #one bottom after one account
    else: #all at once
        alls = Account.objects.all()
        for i in alls:
            i.approved = 1
            i.save()
        return render(request,"paroll/main.html")     #return alls
                            #one bottom after all account showed
    #press bottom to approve paycheck
    account = Account.objects.get(identity = token) #id should be return
    account.approved = 1
    account.save()
def check_one(request):
    temp=request.POST['toke']
    account = Account.objects.get(identity = temp)
    account.approved = 1
    account.save()
    account = Account.objects.all()
    return render(request,"paroll/approvement_one.html",{'accounts':account})
def unapproved(request):
    alls = Account.objects.all()
    for i in alls:
        i.approved = 0
        i.save()
    return render(request,"paroll/main.html")

def change_data(request):
    temp=request.POST['toke']
    account = Account.objects.get(identity = temp) #id should be return

    temp=request.POST['mail']
    if temp != '':
        account.email = temp
        account.save()

    temp=request.POST['bank']
    if temp != '':
        account.bank_account = temp
        account.save()

    temp=request.POST['address']
    if temp != '':
        account.address = temp
        account.save() #_email,_bank , _address shold be reurn
    return input_data(request)

def export(request):
    account = paycheck.objects.all()
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    j=11
    count = 0
    for i in account:
        temp = 'ID : '
        temp += i.identity
        p.drawString(inch,j*inch,temp)
        j-=0.5

        temp = 'work hour : '
        temp += str(i.work_hour)
        p.drawString(inch,j*inch,temp)
        j-=0.5

        temp = 'deduction : '
        temp += str(i.deduction)
        p.drawString(inch,j*inch,temp)
        j-=0.5

        temp = 'salary : '
        temp += str(i.salary)
        p.drawString(inch,j*inch,temp)
        j-=0.5
        count+=1
        if count == 4:
            j = 10
            count = 0
            p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
# Create your views here.
