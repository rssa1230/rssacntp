from django.forms import ModelForm
from django import forms
from pengurus.models import Data

class FormData(ModelForm):
    class Meta:
        model = Data
        fields = '__all__'

        widgets = {
            'nis' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'kelas' : forms.Select({'class':'selectpicker form-control', 'data-live-search':'true'}),
            'keterangan' : forms.Select({'class':'form-control'}),
            'jabatan' : forms.TextInput({'class':'form-control'}),
            'proker' : forms.Textarea({'class':'form-control'}),
        }

