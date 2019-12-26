from django.contrib import admin
from .models import Account,paycheck

class PaycheckInline(admin.TabularInline):
    model = paycheck
    extra = 0
    
class AccountAdmin(admin.ModelAdmin):
    inlines = [PaycheckInline]

admin.site.register(Account, AccountAdmin)
admin.site.register(paycheck)
# Register your models here.
