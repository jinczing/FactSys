from django.contrib import admin
from .models import Account, ApplicationState, Schedule, ScheduleState

class ApplicationStateInline(admin.TabularInline):
    model = ApplicationState
    extra = 0
    
class AccountAdmin(admin.ModelAdmin):
    inlines = [ApplicationStateInline]

class ScheduleStateInline(admin.TabularInline):
    model = ScheduleState
    extra = 0
    
class ScheduleAdmin(admin.ModelAdmin):
    inlines = [ScheduleStateInline]

admin.site.register(Account, AccountAdmin)
admin.site.register(ApplicationState)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(ScheduleState)

# Register your models here.
