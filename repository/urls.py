from django.urls import path
from .views import predictFoodView, dietSaveView, dietSelectView, trainSaveView, trainSelectView, dietVisView

app_name = 'repository'
urlpatterns = [
    path('predict', predictFoodView, name='prediction'),
    path('dietsave', dietSaveView, name='dietsave'),
    path('dietselect', dietSelectView, name='dietselect'),
    path('dietvis', dietVisView, name='dietvis'),
    path('trainsave', trainSaveView, name='trainsave'),
    path('trainselect', trainSelectView, name='trainselect'),
]
