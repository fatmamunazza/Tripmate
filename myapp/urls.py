from django.urls import path
from . import views


urlpatterns = [

    path('', views.index),
    path('tripMateForm/', views.tripmateform, name="tripMateForm"),
    path('check', views.check, name="check"),
    path('selectedList/<str:id>/<int:id1>', views.selectedList, name="selectedList/<str:id>/<int:id1>"),
    path('selectedList/selected/detailsPage', views.detailsPage, name="detailsPage"),
]
