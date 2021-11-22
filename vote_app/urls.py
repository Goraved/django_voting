from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_vote', views.submit_vote, name='submit_vote'),
    path('get_query', views.get_query, name='get_query'),
]
