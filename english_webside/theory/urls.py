from django.urls import path
from . import views

urlpatterns = [
    path("", views.theory_start, name="theory-start"),
    path("phonetics", views.phonetics, name="phonetics"),
    path("alphabet", views.alphabet, name="alphabet"),
    path("numbers", views.numbers, name="numbers"),
    path("time", views.time, name="time"),
    path("present", views.present, name="present"),
    path("past", views.past, name="past"),
    path("future", views.future, name="future"),
    path("irregular", views.irregular_verb, name="irregular-verb"),

]