from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
Congestion_Type =(
    ("low",'LOW'),
    ("moderate","MODERATE"),
    ("high","HIGH"),
    ("very high","VERY HIGH"),
    ("closed","CLOSED" ),
)
Category_Type=(
    ("PARK","park"),
    ("MUSEUM","museum"),
    ("MONUMENT","monument"),
    ("WORSHIP","worship"),
    ("LAKE","lake"),
    ("LIBRARY","library"),
    ("AMUSEMENT","amusement"),
    ("HOTEL","hotel"),
    ("ZOO","zoo"),
)
class state(models.Model):
    name =models.CharField(max_length=50, unique=True)
    class Meta:
        verbose_name = "States"

    def __str__(self):
        return self.name

class city(models.Model):
    stateCity=models.ForeignKey(state,verbose_name = "States",on_delete=models.CASCADE)
    city = models.CharField(max_length=50, unique=True)
    class Meta:
        verbose_name = "City"

    def __str__(self):
          return self.city

class Category(models.Model):
    cityCategory = models.ForeignKey(city, verbose_name="City", on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=Category_Type, default='PARK')
    placesList = models.CharField(max_length=40, unique=True)
    address = models.CharField(max_length=100)
    distance = models.FloatField(max_length=3)
    congestion = models.CharField(max_length=10, choices=Congestion_Type, default='LOW')

    class Meta:
        verbose_name = "Categories"

    def __str__(self):
        return self.placesList

class PublicPlaces(models.Model):
    categoryPlaces = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)
    placeName = models.CharField(max_length=40, unique=True)
    address = models.CharField(max_length=100)
    distance = models.FloatField(max_length=3)
    rating = models.FloatField(max_length=3)
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    coordinates1 = models.FloatField(max_length=8,default=2.2)
    coordinates2 = models.FloatField(max_length=8,default=2.2)
    opentime=models.TimeField(auto_now=False,auto_now_add=False,default='9:00')
    closedtime=models.TimeField(auto_now=False,auto_now_add=False,default='12:00')
    description= models.CharField(max_length=250 ,default=" ")
    congestion = models.CharField(max_length=10,choices=Congestion_Type,default='LOW')

    class Meta:
        verbose_name = "PublicPlaces"

    def __str__(self):
          return self.placeName
