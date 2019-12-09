from .models import BankAccount
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def list(request):
	accounts = BankAccount.filter(client=request.user)
	render(request, 'web/accounts/list.html', locals())