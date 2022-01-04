from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("calendar/<int:year>/<str:month>", views.calendar, name="calender")
]

"""
Path converters:
- int: numbers
- str: strings
- path: whole urls /
- slug: hyphen-and_underscores_staff
- UUID: universally unique identifier
"""