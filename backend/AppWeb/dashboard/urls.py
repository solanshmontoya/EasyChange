from django.urls import path
from . import views_bank_account
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('panel/', views.dashboard, name='dashboard'),
    path('transaction/', views.information, name='transaction'),
    path('confirm-transaction/', views.confirm_transaction, name='confirm-transaction'),
    path('bank-accounts/', views_bank_account.enlist, name='bank_account_list'),
    path('bank-accounts/new/', views_bank_account.add, name='bank_account_add')

]