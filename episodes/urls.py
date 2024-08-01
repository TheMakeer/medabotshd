from django.urls import path

from . import views

app_name = 'episodes'

urlpatterns = [
    path('', views.all_episodes, name='episodes'),
    path('episode/<int:id>', views.episode, name='episode'),
]
