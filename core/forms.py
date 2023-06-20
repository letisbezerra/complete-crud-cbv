from django import forms
from django.forms import ModelForm
from core.models import Cliente
from cpf_field.models import CPFField
from .models import *
from core.forms import ModelForm

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
