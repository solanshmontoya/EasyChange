from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from enterprise import models
from dashboard import forms
from django.contrib.auth.decorators import permission_required

@login_required
#@permission_required('core.enlist_bank_account')
# @user_passes_test(lambda u: u.is_superuser or u.is_staff)
def enlist(request):
    items = models.BankAccount.objects.all()
    print(items)
    return render(request, 'dashboard/bankAccounts/list.html', locals())


#@login_required
# @user_passes_test(lambda u: u.is_superuser or u.is_staff)
def show(request):
    return render(request, 'dashboard/bankAccounts/form.html', locals())


@login_required
#@permission_required('core.add_BankAccount')
# @user_passes_test(lambda u: u.is_superuser or u.is_staff)
def add(request):
    is_creating = True
    if request.POST:
        form = forms.BankAccountForm(request.POST, request.FILES)
        if form.is_valid():
            account = form.save(commit=False)
            account.client = request.user #con estto 
            account.save()
            return redirect(reverse('dashboard:bank_account_list'))
    else:
        form = forms.BankAccountForm()
    return render(request, 'dashboard/bankAccounts/form.html', locals())


#@login_required
#@user_passes_test(lambda u: u.is_superuser or u.is_staff)
#@permission_required('core.change_BankAccount')
def edit(request, id):
    title = "Detalle"
    bankAccount = get_object_or_404(models.BankAccount, pk=id)
    if request.POST:
        form = forms.BankAccountForm(request.POST, request.FILES, instance=bankAccount)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard:bankAccounts_list'))
    else:
        form = forms.BankAccountForm(instance=BankAccount)
    return render(request, 'dashboard/bankAccounts/form.html', locals())


#@login_required
#@permission_required('core.delete_BankAccount')
#@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def delete(request, id):
    bankAccount = get_object_or_404(models.BankAccount, pk=id)
    bankAccount.delete()
    messages.success(request, "Eliminado correctamente")
    return HttpResponseRedirect('/admin/bankAccounts')
