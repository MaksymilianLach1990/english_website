from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("calendars/<int:year>/<str:month>/", views.calendars, name="calendars"),
    path("calendars/", views.calendars, name="calendars"),

    path("events", views.all_events, name="list-events"),
    path("add_venue", views.add_venue, name="add-venue"),
    path('list_venues', views.list_venue, name='list-venue'),
    path('show_venue/<venue_id>', views.show_venue, name="show-venue"),
]

"""
Path converters:
- int: numbers
- str: strings
- path: whole urls /
- slug: hyphen-and_underscores_staff
- UUID: universally unique identifier
"""