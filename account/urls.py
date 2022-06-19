from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name = 'register'),
    path('profile/', profile, name = 'profile'),
    path('update/', update, name = 'update')
]