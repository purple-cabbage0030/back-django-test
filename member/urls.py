from django.urls import path

from .views import registrationView, userView

app_name = 'member'
urlpatterns = [
    path('register', registrationView, name='register'),
    path('userinfo', userView, name='userinfo'),
]