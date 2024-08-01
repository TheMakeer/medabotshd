from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse

from itertools import chain

from .services import get_all_characters, find_character, find_medarot, get_detail

def all_characters(request):
    characters = get_all_characters()

    return render(request, 'characters.html',{
        'characters': characters,
    })

def search_character(request):

    query = request.GET.get('q', '')

    characters = find_character(query)
    medarots = find_medarot(query)

    results = list(chain(characters, medarots))

    html = render_to_string('characters_list.html', {'characters': results})

    return JsonResponse({ 'html': html })


def detail(request):

    name_and_id = request.GET.get('name_with_id', '')

    character, kind = get_detail(name_and_id)

    print(character, kind)

    html = render_to_string('character_detail.html', {'character': character, 'kind':kind})

    return JsonResponse({ 'html': html })

