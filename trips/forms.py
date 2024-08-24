from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = [
            'title', 'description', 'image', 'cost', 'location',
        ]
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'image': 'Изображение',
            'cost': 'Стоимость',
            'location': 'Местоположение',
        }