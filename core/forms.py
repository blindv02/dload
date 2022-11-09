from django import  forms
from .models import Historia_descarga




# Agregado por Leo para hacer el historial de desacarga#
######################## 5/11/2022 #####################
class HistoriaForm(Historia_descarga):
    #fecha = forms.DateField(widget=forms.DateField)
    #vurl = forms.URLField()
    #Formato = forms.CharField()
    #tipovideo = forms.CharField()
    #usuario = forms.CharField()
    
    class meta:
        model = Historia_descarga
        fields = ['fecha','user_email', 'tipo_descarga','descargas', 'url','titulo']
        
        
    