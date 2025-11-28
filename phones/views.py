
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog', permanent=True)


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phones':phone}
    return render(request, template, context)

