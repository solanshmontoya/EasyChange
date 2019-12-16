from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from enterprise.models import Coin, BankAccount, Company

def home(request):
	coins = Coin.objects.all()
	coin = request.GET.get('coin')
	if coin:
		coin_selected = Coin.objects.get(name=coin)
		company = Company.objects.all().first() #Here is the company 
		if company:
			company_bank_accounts = BankAccount.objects.filter(client=company.owner)
		if request.user.is_authenticated:
			bank_accounts = BankAccount.objects.filter(client=request.user)
	return render(request, 'dashboard/home.html', locals())

def dashboard(request):
	return render(request, 'dashboard/home.html', locals())

@login_required
def information(request):
	company = Company.objects.all().first()
	return render(request, 'dashboard/information.html', locals())

@login_required
def confirm_transaction(request):
	return render(request, 'dashboard/confirm_transaction.html', locals())
