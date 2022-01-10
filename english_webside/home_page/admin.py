from django.contrib import admin
from .models import Venue, MySiteUser, Event

# Register your models here.


# admin.site.register(Venue)
admin.site.register(MySiteUser)
# admin.site.register(Event)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone') # pokazuje kolumny w panelu admin
    ordering = ('name',) # jesli dodasz '-' przed nazwą lista będzie odwrócona sortuje listę
    search_fields = ('name', 'address') # pole do wyszukiwania określonych kolumn

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'description', 'manager') # rozdzielanie poszczególnych informacji
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue') # filtrowanie listy
    ordering = ('event_date',)