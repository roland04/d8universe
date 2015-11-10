from django.contrib import admin

from .models import Universe, UniverseCreator, Attribute, Ability, Race, StartAttribute

class UniverseAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,          {'fields': ['name']}),
            ('Attributes',   {'fields': ['attributes'], 'classes': ['collapse']}),
            ('Abilities',   {'fields': ['abilities'], 'classes': ['collapse']}),
        ]
    filter_horizontal = ('attributes','abilities')

class StartAttributeAdmin(admin.ModelAdmin):
    fields = ['universe','race','attribute','value']

class UniverseCreatorAdmin(admin.ModelAdmin):
    fields = ['universe','user','role']

admin.site.register(Universe,UniverseAdmin)
admin.site.register(UniverseCreator,UniverseCreatorAdmin)
admin.site.register(Attribute)
admin.site.register(Ability)
admin.site.register(Race)
admin.site.register(StartAttribute,StartAttributeAdmin)
