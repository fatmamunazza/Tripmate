from django.urls import path
from . import views


urlpatterns = [

    path('', views.index),
    path('tripMateForm/', views.tripmateform, name="tripMateForm"),
    path('check', views.check, name="check"),
    path('selectedList/<str:id>/<int:id1>', views.selectedList, name="selectedList"),
    path('selectedList/<str:list>/detailsPage/<int:value>', views.detailsPage, name="detailsPage"),
]
