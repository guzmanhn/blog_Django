from django import forms
from .models import comment


class FormComment(forms.ModelForm):
	class Meta:
		model = comment
		exclude = ["idEntrada"]
		#fields = ['idEntrada','autor', 'mensaje']

