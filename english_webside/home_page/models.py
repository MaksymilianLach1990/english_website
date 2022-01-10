from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=50)
    phone = models.CharField('Contact Phone', max_length=25, blank=True)
    web = models.URLField('Website Address', blank=True)
    email_address = models.EmailField('Email Address', blank=True)

    def __str__(self):
        return self.name


class MySiteUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

# Nadaj nazwę i dodaj models.Model
class Event(models.Model):
    # nazwij kolumny
    # 
    name = models.CharField('Event Name', max_length=120) # charakters fild 'text'(nadaj nazwę, określ długość w znakach)
    event_date = models.DateTimeField('Event Date') # data i czas
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE) # CASCADE usuń wszystko co jest poniżej połączone z tym
    # venue = models.CharField(max_length=120)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL) # jeśli menarzer zostanie usunięty z listy, pole pozostanie puste
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MySiteUser, blank=True)

    # pokazuje dane w panelu administratora
    def __str__(self):
        return self.name
