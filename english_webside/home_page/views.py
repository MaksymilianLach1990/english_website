from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, UserMessage

# Create your views here.



def home(request):
    return render(request, 'home_page/home.html', {})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        uMess = UserMessage(username=message_name, email=message_email, date_post=datetime.now(), text=message)
        uMess.save()
        return render(request, 'home_page/contact.html', {'message_name': message_name})

    else:
        return render(request, 'home_page/contact.html', {})

def calendars(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    events = Event.objects.all() # lista aktualności na stronie 
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
        "events": events
    })

