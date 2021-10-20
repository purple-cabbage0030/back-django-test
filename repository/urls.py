from django.urls import path, include
from .views import helloAPI, predictFoodView, dietSaveView

app_name = 'repository'
urlpatterns = [
    path('hello', helloAPI, name='hello'),
    path('predict', predictFoodView, name='prediction'),
    path('dietsave', dietSaveView, name='dietsave')
]