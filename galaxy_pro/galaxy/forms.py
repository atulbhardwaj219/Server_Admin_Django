from django import forms
from .models import Servers,Request

class AddServer(forms.ModelForm):

    class Meta:
        model=Servers
        fields=['Instancename','ip','port','username','password','OsType']
