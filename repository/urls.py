from django.urls import path
from .views import predictFoodView, dietView, dietVisView, trainView

app_name = 'repository'
urlpatterns = [
    path('predict', predictFoodView, name='predict'),
    path('diet', dietView, name='diet'),
    path('dietvis', dietVisView, name='dietvis'),
    path('train', trainView, name='train'),
]
