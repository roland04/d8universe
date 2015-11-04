from django.contrib import admin

from .models import Universe, Atribute, Ability, Race, StartAtribute

class UniverseAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,          {'fields': ['name']}),
            ('Atributes',   {'fields': ['atributes'], 'classes': ['collapse']}),
            ('Abilities',   {'fields': ['abilities'], 'classes': ['collapse']}),
        ]
    filter_horizontal = ('atributes','abilities')

class StartAtributeAdmin(admin.ModelAdmin):
    fields = ['universe','race','atribute','value']

admin.site.register(Universe,UniverseAdmin)
admin.site.register(Atribute)
admin.site.register(Ability)
admin.site.register(Race)
admin.site.register(StartAtribute,StartAtributeAdmin)
