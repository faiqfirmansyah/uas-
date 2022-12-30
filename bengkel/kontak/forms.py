from django.forms import ModelForm
from django import forms
from .models import kon

class formkon(ModelForm):
    class Meta:
        model = kon
        fields = '__all__'


        widgets = {
            'N_register': forms.TextInput({'class':'form-control'}),
            'Nama': forms.TextInput({'class':'form-control'}),
            'Alamat': forms.TextInput({'class':'form-control'}),
            'Keterangan': forms.TextInput({'class':'form-control'}),
        }