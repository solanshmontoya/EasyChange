from django.contrib import admin
from .models import Bank, Company, Coin, BankAccount
# Register your models here.
admin.site.register(Bank)
admin.site.register(Company)
admin.site.register(Coin)
admin.site.register(BankAccount)
