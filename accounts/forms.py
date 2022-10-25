from django import  forms
from .models import Usuario


class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese Password',
        'class': 'form-control',
    }))

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email']

    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args,**kwargs)
        self.fields['nombre'].widget.attrs['placeholder'] = 'Ingrese nombre'
        self.fields['apellido'].widget.attrs['placeholder'] = 'Ingrese apellidos'
        self.fields['email'].widget.attrs['placeholder'] = 'Ingrese email'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

    """
    def clean(self):
       cleaned_data = super(RegistroForm, self).clean()
       password = cleaned_data.get('password')
       confirm_password = cleaned_data.get('confirm_password')

       if password != confirm_password:
           raise forms.ValidationError(
                "El password no coincide!"
           )
"""

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre', 'apellido',)

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

