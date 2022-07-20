
from django.forms import ModelForm,TextInput
from .models import City
from .models import addNotes

#To add notes to database
class NoteForm(ModelForm):
    class Meta:
        model = addNotes
        fields = ['notes']
        widgets ={'notes':TextInput(attrs={'class':'input','placeholder':'Enter Notes'})}
    
#To add city
class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets ={'name':TextInput(attrs={'class':'input','placeholder':'Add City'})}
    

