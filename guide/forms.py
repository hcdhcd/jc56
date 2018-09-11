from django import forms
from guide import views
from .models import Commentaire, Jeu

my_default_errors = {
	'required': '',
	
}

class CommentaireForm(forms.ModelForm):
	commentaire= forms.CharField(widget= forms.Textarea(attrs={'cols': 120, 'rows': 10}), label='', required=True, error_messages=my_default_errors)
	date=forms.DateTimeField(widget=forms.HiddenInput, required=False, )
	pseudo=forms.ModelChoiceField(queryset=None, widget=forms.HiddenInput, required=False)


	class Meta:
		model = Commentaire
		fields = '__all__'

		widgets = {'jeu': forms.HiddenInput, 'article': forms.HiddenInput, 'lien' : forms.HiddenInput ,
					 'date' : forms.HiddenInput, 'pseudo': forms.HiddenInput, 'GarsSur' : forms.HiddenInput , }






class JeuForm(forms.ModelForm):

	field_order = ('nom', 'multi', 'solo', 'censure', 'developpeur', 'editeur')

	def __init__(self, *args, **kwargs):
		super(JeuForm, self).__init__(*args, **kwargs)

		for key in self.fields:
			self.fields[key].required = False 

	
	class Meta:
		model = Jeu
		exclude = ('slug', 'photo', 'datesortie', 'nomVO', 'test')
		widgets = {'genre' : forms.CheckboxSelectMultiple,}
	