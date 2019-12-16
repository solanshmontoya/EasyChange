from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

BANK_ACCOUNT_TYPE = (
	(1, 'ahorros'),
	(2, 'corriente'),
)
TRANSACTION_STATE = (
	(1, 'iniciado'), # the user init the operation
	(2, 'por confirmar'), # when the user make the transfer and update the operation number
	(3, 'confirmado'), # when the company approve the money received
	(4, 'completado'), # when the company make the transfer  
	(5, 'rechazado') # when the company reject the operation, for example when the opertaion number is wrong
)

class Company(models.Model):
	class Meta:
		verbose_name = 'CuentaEmpresa'
	ruc = models.CharField('RUC', max_length = 11, blank=True, null=True)
	name = models.CharField('Nombre', max_length=50, blank=True, null=True)
	account_number_company = models.TextField('Cuentas Bancarias', blank=True, null=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.name

#for client bank account
class Bank(models.Model):
	name = models.CharField(max_length=50)

#client bank account 
class BankAccount(models.Model):
	client = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField('Nombre de la Cuenta', max_length = 100)
	bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
	number = models.CharField(max_length=100)
	type = models.IntegerField(choices=BANK_ACCOUNT_TYPE)
 
class Coin(models.Model):
	name = models.CharField(max_length=20)
	symbol = models.CharField(max_length=5) # s/. $ E
	exchange_rate_sale = models.DecimalField("Venta", max_digits=10, decimal_places=2) #3.4   |  4
	exchange_rate_purchase = models.DecimalField("Compra", max_digits=10, decimal_places=2) #3.5   | 4.1
	

class Transaction(models.Model):
	class Meta:
		verbose_name = 'Transaccion'
	#choosen (elegir de las cuentas que ingrese el usuario)
	#receptionAccount = 
	coin_transform = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='coin_transform')
	operation_type = models.CharField(max_length=10)
	exchange_rate = models.DecimalField("Exchange", max_digits=10, decimal_places=3) #3.4   |  4
	amount_from = models.DecimalField('Inicial', max_digits=10, decimal_places=2)
	amount_to = models.DecimalField('Final', max_digits=10, decimal_places=2)
	client_bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='client_bank_account') #for receive the money
	company_bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='company_bank_account') # for sent the money
	operation_number = models.CharField(max_length=20)
	state = models.IntegerField(TRANSACTION_STATE, default=1)
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
