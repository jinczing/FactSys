from django.urls import path

from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('showpaycheck/', views.show_paycheck, name='show_paycheck'),
    path('inputdata/', views.input_data, name='input_data'),
    path('approvement/', views.approvement, name='approvement'),
    path('check/', views.check, name='check'),
    path('changedata/', views.change_data, name='change_data'),
    path('checkone/', views.check_one, name='check_one'),
    path('unapproved/', views.unapproved, name='unapproved'),
    path('export/', views.export, name='export')
]
