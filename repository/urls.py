from django.urls import path, include
from .views import helloAPI, predictFood

app_name = 'repository'
urlpatterns = [
    path('hello/', helloAPI, name='hello'),
    path('predict/', predictFood, name='prediction')
]