from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')

    if sort == 'name':
        phone = sorted(Phone.objects.all(), key=lambda p: p.name)

    if sort == 'min_price':
        phone = sorted(Phone.objects.all(), key=lambda p: p.price)

    if sort == 'max_price':
        phone = sorted(Phone.objects.all(), key=lambda p: p.price, reverse=True)

    context = {
        'phones': phone
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.filter(slug=slug) # как привести тип QuerySet в тип Phone?
    }
    print(context)
    return render(request, template, context)
