from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home_page/home.html', {})

def contact(request):
    return render(request, 'home_page/contact.html', {})

def calendar(request, year, month):
    return render(request, 
    'home_page/calendar.html', {})