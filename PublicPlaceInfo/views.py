from django.shortcuts import render
from django.utils import translation
from django.utils.translation import ugettext_lazy as _

# Create your views here.

def publicPlaceList(request):
    language = request.POST.get('language', 'default')

    if language == "Hindi":
        translation.activate('hi')
    else:
        translation.activate('en-us')
    return render(request, 'publicPlaceList.html')