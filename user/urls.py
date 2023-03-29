from django.urls import path
from .views import login_view, logout_view, register

app_name = 'user'

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('register/', register, name='register'),
]