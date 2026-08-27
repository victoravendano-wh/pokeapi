from django import forms  

class CantidadPokemonForm(forms.Form):
    cantidad = forms.IntegerField(max_value=1024, min_value=1)