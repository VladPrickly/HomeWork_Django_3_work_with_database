from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog', permanent=True)


def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get('sort', '')
    all_phones = Phone.objects.all()

    if sort_pages == 'name':
        phone = all_phones.order_by('name')
        context = {'phones': phone}
        return render(request, template, context)

    elif sort_pages == 'min_price':
        phone = all_phones.order_by('price')
        context = {'phones': phone}
        return render(request, template, context)

    elif sort_pages == 'max_price':
        phone = all_phones.order_by('-price')
        context = {'phones': phone}
        return render(request, template, context)

    context = {'phones': all_phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phones': phone}
    return render(request, template, context)