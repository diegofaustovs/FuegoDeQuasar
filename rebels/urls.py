from django.urls import path
from . import views

urlpatterns = [
    path('topsecret', views.get_position_and_message, name='topsecret'),
    # path('', views.index, name='index'),
    # path('error', views.err, name='error'),
]
