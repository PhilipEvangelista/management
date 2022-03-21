import datetime

from django.shortcuts import render, redirect
from .models import *
from .forms import SecurityCheck, InformationEdit, InformationCreate
from calendar import monthrange


def home(response):
    return render(response, "home.html")


def list_client(response):
    active()
    ls = Information.objects.all()
    if 'search' in response.GET:
        if response.GET["search"] != '':
            search = response.GET["search"]
            ls = Information.objects.filter(name__icontains=search)
    return render(response, "list_client.html", {'item': ls})


def profile(response, pk):
    active()
    if Information.objects.filter(id=int(pk)).exists():
        ls = Information.objects.get(id=int(pk))
        return render(response, 'profile.html', {'item': ls})
    else:
        return render(response, "home.html")


def status(response):
    active()
    ls = Information.objects.all()
    return render(response, 'status.html', {"item": ls})


def secure(response):
    active()
    forms = SecurityCheck()
    if response.method == 'POST':
        if Security.objects.filter(username=response.POST['username'], password=response.POST['password']).exists():
            return redirect('owner/')
    return render(response, 'secure.html', {"form": forms})


def owner(response):
    active()
    ls = Information.objects.all()
    if 'search-item' in response.GET:
        if response.GET["search-item"] != '':
            search = response.GET["search-item"]
            ls = Information.objects.filter(name__icontains=search)
    return render(response, "owner.html", {'item': ls})


def edit(response, pk):
    active()
    ls = Information.objects.get(id=pk)
    form = InformationEdit(instance=ls)
    if response.method == 'POST':
        form = InformationEdit(response.POST, instance=ls)
        if form.is_valid():
            form.save()
        return redirect("owner")

    return render(response, 'edit.html', {'forms': form})


def update(response, pk):
    active()
    ls = Information.objects.get(id=pk)
    if response.method == "POST":
        if response.POST['get_option'] == 'Add Debts':
            ls.balance += float(response.POST['get-amount'])
        else:
            ls.balance -= float(response.POST['get-amount'])
        if float(response.POST['get-amount']) >= ls.balance / 4:
            ls.date = timezone.now()
        ls.save()
        return redirect("owner")
    return render(response, "update.html", {"item": ls, 'time': datetime.date.today()})


def delete(response, pk):
    ls = Information.objects.get(id=pk)
    if response.method == 'POST':
        ls.delete()
        return redirect("owner")
    return render(response, 'delete.html', {"item": ls})


def active():
    ls = Information.objects.all()
    for i in ls:
        sm = Information.objects.get(id=i.id)
        date = monthrange(sm.date.year, sm.date.month)
        date_now = datetime.date.today() - sm.date.date()
        if i.interest_bool and date_now.days > date[1]:
            interest = datetime.date.today() - sm.date.date()
            interest = interest.days - date[1]
            balance = interest + sm.balance
            sm.balance = balance
            sm.interest = interest
            sm.date_debts = timezone.now()
            sm.interest_bool = False
        else:
            date = datetime.date.today() - sm.date_debts.date()
            if date.days > 0:
                interest = date.days + sm.interest
                balance = date.days + sm.balance
                sm.balance = balance
                sm.interest = interest
                sm.date_debts = datetime.date.today()
        sm.save()


def create(response):
    forms = InformationCreate()
    if response.method == 'POST':
        forms = InformationCreate(response.POST)
        if forms.is_valid():
            forms.save()
            return redirect("home")
    return render(response, "create.html", {'form': forms})