from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    title = models.CharField('Title event', max_length=255, blank=True)
    date_start = models.DateTimeField('Event data', null=True, blank=True)
    describe = models.TextField('Describe', null=True, blank=True)

    def __str__(self):
        return self.title

# Nadaj nazwę i dodaj models.Model
# class Event(models.Model):
#     # nazwij kolumny
#     # 
#     name = models.CharField('Event Name', max_length=120) # charakters fild 'text'(nadaj nazwę, określ długość w znakach)
#     event_date = models.DateTimeField('Event Date') # data i czas
#     venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE) # CASCADE usuń wszystko co jest poniżej połączone z tym
#     # venue = models.CharField(max_length=120)
#     manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL) # jeśli menarzer zostanie usunięty z listy, pole pozostanie puste
#     description = models.TextField(blank=True)
#     attendees = models.ManyToManyField(MySiteUser, blank=True)

#     # pokazuje dane w panelu administratora
#     def __str__(self):
#         return self.name
