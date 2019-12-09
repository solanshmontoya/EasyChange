from django.urls import path
from . import views
from . import views_bank_accounts

app_name = 'web'

urlpatterns = [
    path('', views.home, name='home'),
]