from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('change/', views.change, name='change'),
    path('apply/', views.apply, name='apply'),
    path('approve/', views.approve, name='approve'),
    path('main/', views.main, name='main'),
    path('<str:trans_type>/transfer/', views.transfer, name='transfer'),
    path('schedule/', views.schedule, name='schedule'),
    path('account_manage/', views.account_manage, name='account_manage'),
]



# Create your views here.
