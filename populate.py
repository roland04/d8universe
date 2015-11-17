import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd8universe.settings')

import django
django.setup()

from universes.models import Attribute, Ability, Feature, Universe, UniverseManager, Race, RaceAttribute

def populate():
    add_attribute("Fortaleza", "For")
    add_attribute("Agilidad", "Agi")
    add_attribute("Astucia", "Ast")
    add_attribute("Inteligencia", "Int")
    add_attribute("Apariencia", "Apa")
    add_attribute("Voluntad", "Vol")

def add_attribute(name, short_name, description=""):
    a = Attribute.objects.get_or_create(name=name, short_name=short_name, description=description)[0]
    print('Atribute "%s" created' % (a.name))

if __name__ == '__main__':
    print("Starting d8universe population script...")
    populate()
