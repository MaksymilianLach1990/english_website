from django.contrib import admin
from .models import IrregularVerb
# Register your models here.

@admin.register(IrregularVerb)
class EventAdmin(admin.ModelAdmin):
    fields = ('name_pl', ('name_en_1', 'spell_1'), ('name_en_2', 'spell_2'), ('name_en_3', 'spell_3'))
    list_display = ('name_pl', 'name_en_1')
    ordering = ('name_en_1',)
    search_fields = ('name_pl', 'name_en_1')