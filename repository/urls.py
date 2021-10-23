from django.urls import path, include
from .views import predictFoodView, dietSaveView, dietSelectView, trainSaveView

app_name = 'repository'
urlpatterns = [
    path('predict', predictFoodView, name='prediction'),
    path('dietsave', dietSaveView, name='dietsave'),
    path('dietselect', dietSelectView, name='dietselect'),
    path('trainsave', trainSaveView, name='dietsave'),
]
