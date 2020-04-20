from django.contrib import admin
from myapp.models import *

# Register your models here.

admin.site.register(state)
admin.site.register(city)
admin.site.register(Category)
admin.site.register(PublicPlaces)