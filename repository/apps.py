from django.apps import AppConfig
from tensorflow.keras import models


class ApiConfig(AppConfig):
    name = 'repository'
    model = models.load_model(r'./classification_model/best_model_.h5')