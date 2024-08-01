from django.urls import path

from .views import all_characters, search_character, detail

app_name = 'characters'

urlpatterns = [
    path('', all_characters, name='characters'),
    path('search/', search_character, name='search'),
    path('detail/', detail, name='detail'),
]
