from django.urls import path
from .views import index
from .views import login

app_name = 'dashboard'
urlpatterns = [
    
    path('/home', index, name='index'),
    path('', login, name='login')
    
]
