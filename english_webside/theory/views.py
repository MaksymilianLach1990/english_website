from django.shortcuts import render
from .models import IrregularVerb

# Create your views here.

def load_info(plik):
    with open(plik, 'rb') as f:
        text = f.readlines()
        letters = []
        for line in text:
            line = line.strip().decode('utf-8').split(',')
            letters.append(line)
        
        return letters



# print(load_alphabet('english_webside/theory/alphabet.txt'))

def theory_start(request):
    return render(request, 'theory/theory_start.html', {})

def phonetics(request):
    return render(request, 'theory/phonetics.html', {})

def alphabet(request):
    letters = load_info('theory/information/alphabet.txt')
    return render(request, 'theory/alphabet.html', {
        'letters': letters
        })

def numbers(request):
    numbers = load_info('theory/information/numbers.txt')
    return render(request, 'theory/numbers.html', {
        'numbers': numbers
        })

def time(request):
    return render(request, 'theory/present.html', {})

def present(request):
    return render(request, 'theory/present.html', {})

def past(request):
    return render(request, 'theory/past.html', {})

def future(request):
    return render(request, 'theory/future.html', {})

def irregular_verb(request):
    irregular_verb = IrregularVerb.objects.all()
    return render(request, 'theory/irregular_verb.html', {
        'irregular_verb': irregular_verb
        })
