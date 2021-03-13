from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from data_import.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('data_import.urls'), name='data_import'),
    path('home/', home, name='home'),
    path('', include('user.urls'), name='user'),
    path('', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
]
