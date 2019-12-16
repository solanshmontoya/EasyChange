from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from enterprise.models import Coin, BankAccount, Company, Transaction
import decimal

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
	#if request.POST:
	#	amount_from = request.POST.get('coinFromValue')
	#	coin_selected_id = request.POST.get('coinSelected')
	#	bank_acount_selected_id =  request.POST.get('bankAccountSelected')
	#	operation =  request.POST.get('operation')

	#	coin_selected = Coin.objects.get(id=coin_selected_id)
#		if operation == 'SELL':
#			amount_to = coin_selected.exchange_rate_sale * decimal.Decimal(amount_from)
#			exchange_rate = coin_selected.exchange_rate_sale
#		else:
#			amount_to = coin_selected.exchange_rate_purchase * decimal.decimal(amount_from)
#			exchange_rate = coin_selected.exchange_rate_purchase


	#	transaction = Transaction(coin_transform=coin_selected, 
	#		operation_type= operation, 
	#		exchange_rate =exchange_rate, 
	#		amount_from=amount_from,
	#		amount_to=amount_to,
	#		client_bank_account__id=bank_acount_selected_id
#

#			)
#
#		transaction.save()
#		return render(request, 'dashboard/information.html', locals())
	return render(request, 'dashboard/information.html', locals())

@login_required
def confirm_transaction(request):
	return render(request, 'dashboard/confirm_transaction.html', locals())

def nosotros(request):
	return render(request, 'dashboard/nosotros.html', locals())

def blog(request):
	return render(request, 'dashboard/blog.html', locals())

def ayuda(request):
	return render(request, 'dashboard/ayuda.html', locals())