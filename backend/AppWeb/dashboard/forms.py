from common.forms import BootstrapStyleForm
from enterprise import models


class BankAccountForm(BootstrapStyleForm):
    class Meta:
        model = models.BankAccount        
        exclude = ('client',)

