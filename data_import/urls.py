from django.urls import path
from . import views

app_name = 'data_import'

urlpatterns = [
    path('import/', views.home, name='home'),
]