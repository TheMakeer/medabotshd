from django.shortcuts import render, get_object_or_404
from .models import Episode

def all_episodes(request):

    episodes = Episode.objects.all()
    
    return render(request, 'episodes.html', {
        'episodes': episodes
    })

def episode(request, id):

    episode = get_object_or_404(Episode, pk=id)
    episodes = Episode.objects.all()

    return render(request, 'episode.html', {
        'episode': episode,
        'episodes': episodes,
    })