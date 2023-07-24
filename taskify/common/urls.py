from django.urls import path
from . import views
from .views import about

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', about, name='about'),
]