from ast import Pass
import requests
from django.shortcuts import redirect, render
from .models import City
from .forms import CityForm 
from .models import addNotes
from .forms import NoteForm

def indexPage(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=00f1b34ccd01e15f4911085c984d1f42'
    city='Port Elizabeth'
    form2 = NoteForm()

    if request.method =='POST':
        form2 = NoteForm(request.POST)
        form2.save()
        form2 = NoteForm()
        
    NotesLst= addNotes.objects.all()

   
    r = requests.get(url.format(city)).json()
    city_weather = {
            'city' : city ,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'] ,
            'icon' : r['weather'][0]['icon'],
        }
    context  = {'city_weather': city_weather, 'form2' : form2, 'NotesLst': NotesLst}
    return render(request,'weather/weather.html',context)

   