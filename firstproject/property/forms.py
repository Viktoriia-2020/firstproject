from django import forms
from property.models import Property


class PropertyForm(forms.ModelForm):
    class Meta:

        model = Property
        fields = [
            'title',
            'region',
            'description',
            'image',
            'lot_area',
            'floor_area',
            'bed_room',
            'bath_room',
            'year_build',
            'floors',
            'garage',
            'luggage',
            'price',

        ]

