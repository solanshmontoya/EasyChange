from django.urls import path
from . import views_bank_account

app_name = 'dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('panel/', views.dashboard, name='dashboard'),
    path('products/', views_bank_account.enlist, name='bank_account_list'),
]