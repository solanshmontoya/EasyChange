from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from enterprise.models import Coin, BankAccount, Company

def home(request):
	coins = Coin.objects.all()
	coin = request.GET.get('coin')
	if coin:
		coin_selected = Coin.objects.get(name=coin)
		company = Company.objects.all().first()
		if company:
			company_bank_accounts = BankAccount.objects.filter(client=company.owner)
		bank_accounts = BankAccount.objects.filter(client=request.user)
	return render(request, 'dashboard/home.html', locals())

#@login_required
def dashboard(request):
	return render(request, 'dashboard/home.html', locals())