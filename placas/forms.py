from django import forms
from .models import Cadastro_lote,Cadastro_placas,Modelo_placas

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo_placas
        fields = '__all__'

class PlacaForm(forms.ModelForm):
    class Meta:
        model = Cadastro_placas
        fields = '__all__'

class LoteForm(forms.ModelForm):
    class Meta:
        model = Cadastro_lote
        fields = '__all__'