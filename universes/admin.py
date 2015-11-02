from django.contrib import admin

from .models import Universe, Atribute, Ability

class UniverseAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,          {'fields': ['name']}),
            ('Atributes',   {'fields': ['atributes'], 'classes': ['collapse']}),
            ('Abilities',   {'fields': ['abilities'], 'classes': ['collapse']}),
        ]
    filter_horizontal = ('atributes','abilities')

admin.site.register(Universe, UniverseAdmin)
admin.site.register(Atribute)
admin.site.register(Ability)
