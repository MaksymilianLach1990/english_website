from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm
from django.http import HttpResponseRedirect
# Create your views here.

def all_events(request):        
    event_list = Event.objects.all()
    return render(request, 'home_page/events.html', {
        'event_list': event_list
    })

def list_venue(request):
    venue_list = Venue.objects.all()
    return render(request, 'home_page/venues.html', {
        'venue_list': venue_list
    })

def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id) # pk= pobieranie primery key
    return render(request, 'home_page/show_venue.html', {
        'venue': venue
    })
    

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'home_page/add_venue.html', {'form': form, 'submitted': submitted})


def home(request):
    return render(request, 'home_page/home.html', {})

def contact(request):
    return render(request, 'home_page/contact.html', {})

def calendars(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    year = int(year)
    name = "Kris"
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    munth_number = int(month_number)

    # Create a calendar
    cal = HTMLCalendar().formatmonth(
        year,
        month_number
    )
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M %p')
    return render(request, 
    'home_page/calendar.html', {
        "name": name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "time": time,
    })

