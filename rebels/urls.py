from django.urls import path
from . import views

urlpatterns = [
    path('topsecret', views.get_position_and_message, name='topsecret'),
    path('topsecret_split', views.retrieve_position_and_message, name='topsecret_split'),
    path('topsecret_split/<str:satellite>', views.get_position_and_message_split, name='topsecret_split')
]
