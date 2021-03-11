from django.urls import path
from . import views

app_name = 'data_import'

urlpatterns = [
    path('', views.home, name='home'),
]