from django.urls import path
from .views import predictFoodView, dietSaveView, dietSelectView, trainSaveView, trainSelectView, dietVisView, dietView

app_name = 'repository'
urlpatterns = [
    path('predict', predictFoodView, name='predict'),
    path('diet', dietView, name='diet'),
    path('dietvis', dietVisView, name='dietvis'),
    path('trainsave', trainSaveView, name='trainsave'),
    path('trainselect', trainSelectView, name='trainselect'),
]
