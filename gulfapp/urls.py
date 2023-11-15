from django.urls import path
from .views import index, deadstock

urlpatterns = [
    path('index/', index, name='index'),
    path('deadstock/', deadstock, name='deadstock')
    # Add any other URL patterns as needed
] 