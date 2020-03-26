from django import forms
from .models import Pizza, PizzaType


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'


class PizzaTypeForm(forms.ModelForm):
    class Meta:
        model = PizzaType
        fields = '__all__'
