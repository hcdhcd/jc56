from django import forms
#from .models import Creer_un_compte
from django.contrib.auth.models import User 

class ConnexionForm(forms.Form):
	
	username = forms.CharField(label ="Nom d'utilisateur ")
	password = forms.CharField(widget=forms.PasswordInput)

class InscriptionForm(forms.Form):

	pseudo= forms.CharField(label="Nom d'utilisateur", max_length=30)
	email=forms.EmailField(label='addresse email')
	emailbis = forms.EmailField(label="Confirmation de votre addresse email")
	password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
	passwordbis = forms.CharField(widget=forms.PasswordInput, label="Confirmation du mot de passe")
	Newsletter = forms.BooleanField(required=False,  label='Si vous souhaitez vous inscrire à la Newsletter')
	ConfirmationMail = forms.BooleanField(required=False,  label="Si vous souhaitez recevoir vos identifiants par email")

	def clean(self):

		cleaned_data = super(InscriptionForm, self).clean()
		pseudo = cleaned_data.get('sujet')
		password = cleaned_data.get('password')
		passwordbis = cleaned_data.get('passwordbis')
		email = cleaned_data.get('email')
		emailbis = cleaned_data.get('emailbis')


		if User.objects.all().filter(username = pseudo ).exists() == True:
			raise forms.ValidationError("Ce pseudonyme est dejà utilisé. ")
		if User.objects.all().filter(email = email ).exists() == True:
			raise forms.ValidationError("Cette addresse email est déja utilisé ! Je sais que tu m'aime au point de vouloir créer pleins de compte, mais malheureusement ca crée des conflits avec la base de donnée... :'(")
		if email != emailbis:
			raise forms.ValidationError("Les addresses email sont différentes")
		if len(password)<8:
			self.add_error("password", "Minimum 8 caractères. ")
		if passwordbis != password :
			raise forms.ValidationError("Les mots de passes ne correspondent pas... Essaie encore ! ")


		return cleaned_data

"""		
	def clean_email(self):
		email= self.cleaned_data['email']
		if User.objects.all().filter(email = email ).exists() == True:
			raise forms.ValidationError("Cette addresse email est déja utilisée! Je sais que tu m'aime au point de vouloir créer pleins de compte, mais malheureusement ca crée des conflits avec la base de donnée... :'(")
		return email

	def clean_emailbis(self):
		email = self.cleaned_data['email']
		emailbis = self.cleaned_data['emailbis']
		if email == emailbis:
			raise forms.ValidationError("Les addresses email sont différentes")
		return emailbis

	def clean_password(self):
		password = self.cleaned_data['password']
		
		if len(password)<8:
			raise forms.ValidationError("Minimum 8 caractères. ")
		return password

	def clean_passwordbis(self):
		password = self.cleaned_data['password']
		passwordbis = self.cleaned_data['passwordbis']
		if passwordbis != password :
			raise forms.ValidationError("Les mots de passes ne correspondent pas... Essaie encore ! ")
		return passwordbis
"""
	



class ContactForm(forms.Form):

	envoyeur = forms.EmailField(label="e-mail", label_suffix="")
	sujet = forms.CharField(max_length=100, label_suffix="")
	message = forms.CharField(widget=forms.Textarea, label_suffix="")
	renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez recevoir une copie par mail.", required=False , label="")





class ConnexionForm(forms.Form):

	username = forms.CharField(label="Nom d'utilisateur", max_length=30)

	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
