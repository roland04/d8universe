from django.contrib import admin

from .models import Universe, UniverseManager, Attribute, Ability, Race, RaceAttribute

class UniverseAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,          {'fields': ['name']}),
            ('Attributes',   {'fields': ['attributes'], 'classes': ['collapse']}),
            ('Abilities',   {'fields': ['abilities'], 'classes': ['collapse']}),
        ]
    filter_horizontal = ('attributes','abilities')

class RaceAttributeAdmin(admin.ModelAdmin):
    fields = ['universe','race','attribute','value']

class UniverseManagerAdmin(admin.ModelAdmin):
    fields = ['universe','user','role']

admin.site.register(Universe,UniverseAdmin)
admin.site.register(UniverseManager,UniverseManagerAdmin)
admin.site.register(Attribute)
admin.site.register(Ability)
admin.site.register(Race)
admin.site.register(RaceAttribute,RaceAttributeAdmin)
