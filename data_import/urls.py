# Utility import
from django.urls import path

# Local import from views
from . import views

app_name = 'data_import' #web app name

'''
URL Routes
1. home: http://wwww.website.com/import
'''
urlpatterns = [
    path('import/', views.home, name='home'),
]