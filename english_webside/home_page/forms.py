from django import forms
from django.forms import ModelForm
from .models import Event



# #create Venue Form
# class VenueForm(ModelForm):
#     # Meta musi być nie zostało wyjaśnione co robi
#     class Meta:
#         # określanie co jest nam potrzebne
#         # z której klasy kożystamy
#         model = Venue
#         # jakie pola będziemy potrzebować
#         fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')
#         # zarządzanie wyglądem formularza
#         # nadanie labelek polą
#         labels = {
#             'name': 'Enter Your Venue Here',
#             # 'address': forms.TextInput(attrs={'class':'form-control'}),
#             # 'zip_code': forms.TextInput(attrs={'class':'form-control'}),
#             # 'phone': forms.TextInput(attrs={'class':'form-control'}),
#             # 'web': forms.TextInput(attrs={'class':'form-control'}),
#             # 'email_address': forms.EmailInput(attrs={'class':'form-control'}),
#         }
#         # Użycie boostrapa do nadania wygladu pola entry
#         widgets = {
#             'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Venue name'}),
#             'address': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Address'}),
#             'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Zip-code'}),
#             'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Phone'}),
#             'web': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Web address'}),
#             'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'})
#         }
