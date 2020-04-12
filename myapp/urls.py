from django.urls import path
from . import views


urlpatterns = [

    path('', views.index),
    path('tripMateForm/', views.tripmateform, name="tripMateForm"),
    path('check', views.check, name="check"),
    path('selectedList', views.selectedList, name="selectedList"),
    path('detailsPage', views.detailsPage, name="detailsPage"),
]
