from django.urls import path, include
from PublicPlaceInfo import views

urlpatterns = [
    path('', views.publicPlaceList),
]