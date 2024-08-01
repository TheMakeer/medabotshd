from .models import Character, Medarot
from django.db.models import Q
from itertools import chain

def get_all_characters():
    characters = Character.objects.all()
    medarots = Medarot.objects.all()

    return list(chain(characters, medarots))

def find_character(query):
    characters = Character.objects.all()

    if query:
        characters = characters.filter(Q(name__icontains=query))

    return characters


def find_medarot(query):
    medarots = Medarot.objects.all()

    if query:
        medarots = medarots.filter(Q(name__icontains=query))

    return medarots



def get_detail(name_and_id):

    character = Character.objects.none()

    name, id = name_and_id.split("_")

    print(name, id)

    try:
        character = Character.objects.get(id=id, name=name)
        kind = 'H'
    except Character.DoesNotExist:
        try:
            character = Medarot.objects.get(id=id, name=name)
            kind = 'M'
        except Medarot.DoesNotExist:
            kind = 'H'
    
    # print(character)

    return [ character, kind ]