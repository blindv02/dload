from django import forms
from .models import Usuarios


class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre','apellido','email','password']
    
    def __init__(self, *args, **kwargs):
        super(UsuariosForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
            self.fields[field].widget.attrs['name']=field.name