from django.urls import path
from . import views

#endpoint
urlpatterns = [
    path('', views.getData),
]