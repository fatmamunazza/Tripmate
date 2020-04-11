from django.shortcuts import render
from django.utils import translation
from django.utils.translation import ugettext_lazy as _


def index(request):
    return render(request, 'index.html')

def tripmateform(request):
    return render(request, 'form.html')

def check(request):
       language = request.POST.get('language', 'default')

       if language == "Hindi":
           translation.activate('hi')
       else:
           translation.activate('en-us')

       return render(request, 'publicPlaceList.html')

def selectedList(request):
    return render(request, 'selectedList.html')

def detailsPage(request):
    return render(request, 'detailsPage.html')



