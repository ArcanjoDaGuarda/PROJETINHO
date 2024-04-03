from django import forms
from .models import *


class RelatorioForm(forms.ModelForm):
    class Meta:
        model = Relatorio
        fields = ['nome', 'mes', 'ano', 'descricao', 'link']

class StatusRelatorioForm(forms.ModelForm):
    class Meta:
        model = StatusRelatorio
        fields = ['concluido']

class StatusAulaForm(forms.ModelForm):
    class Meta:
        model = StatusAula
        fields = ['assistida']
        labels = {'assistida': 'Assistida'}
        widgets = {'assistida': forms.CheckboxInput(attrs={'class': 'form-check-input'})}
        
