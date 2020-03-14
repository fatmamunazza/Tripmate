from django.shortcuts import render
from django.utils import translation
from django.utils.translation import ugettext_lazy as _


def index(request):
    return render(request, 'index.html')

def tripmateform(request):
    return render(request, 'form.html')


