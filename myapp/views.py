from django.core import serializers
from django.shortcuts import render
from django.utils import translation
from django.utils.translation import ugettext_lazy as _

from myapp.models import state, city, Category, PublicPlaces


def index(request):
    return render(request, 'index.html')


def tripmateform(request):
    # state1=state.objects.get(name__iexact='bihar')

    json_serializer = serializers.get_serializer("json")()
    cities = json_serializer.serialize(city.objects.all(), ensure_ascii=False)
    context = {
        'state1': state.objects.all(),
        'cities': cities,
    }
    return render(request, 'form.html', context)


def check(request):
    language = request.POST.get('language', 'default')
    country = request.POST.get('country', 'default')
    state = request.POST.get('state', 'default')
    city = request.POST.get('city', 'default')

    # context={
    #    'munazza': _(language),
    # }

    context = {
        'country': country,
        'state': state,
        'city': city
    }

    if language == "Hindi":
        translation.activate('hi')
    else:
        translation.activate('en-us')

    return render(request, 'publicPlaceList.html', context)


def selectedList(request, id, id1):
    SelectedCategory = Category.objects.filter(category__iexact=id)
    SelectedCategory2 = SelectedCategory.filter(cityCategory=id1)

    i = SelectedCategory2.count
    context = {
        'categories': SelectedCategory2,
        'length': i,
        'list': id
    }

    return render(request, 'selectedList.html', context)


def detailsPage(request,list, value):
    try:
        detail = PublicPlaces.objects.get(categoryPlaces_id__exact=value)
    except PublicPlaces.DoesNotExist:
        detail=None
    context = {
        'details': detail,
    }
    return render(request, 'detailsPage.html',context)
