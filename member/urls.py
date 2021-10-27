from django.urls import path

from .views import registrationView, userSelectView, userUpdateView

app_name = 'member'
urlpatterns = [
    path('register', registrationView, name='register'),
    path('select', userSelectView, name='select'),
    path('update', userUpdateView, name='update'),
]