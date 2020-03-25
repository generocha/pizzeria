from django import forms
from .models import Pizza, PizzaType


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'
