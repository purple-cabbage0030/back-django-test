from django.urls import path

from .views import registrationView

app_name = 'member'
urlpatterns = [
    path('register', registrationView, name='register'),
]