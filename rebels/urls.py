from django.urls import path
from . import views

urlpatterns = [
    path('topsecret', views.getpositionandmessage, name='topsecret'),
    # path('', views.index, name='index'),
    # path('error', views.err, name='error'),
]
