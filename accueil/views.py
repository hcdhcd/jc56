from django.shortcuts import render, redirect, HttpResponseRedirect
from datetime import date, time, datetime
from .forms import ContactForm, ConnexionForm, InscriptionForm
from django.views.generic import TemplateView, ListView
from guide.models import Jeu, Genre
from .models import Profil
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout


def connexion(request):


	error = False


	if request.method == "POST":

		form = ConnexionForm(request.POST)

		if form.is_valid():

			username = form.cleaned_data["username"]

			password = form.cleaned_data["password"]

			user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes

			if user:  # Si l'objet renvoyé n'est pas None

				login(request, user)  # nous connectons l'utilisateur
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

			else: # sinon une erreur sera affichée

				error = True

	else:

		form = ConnexionForm()


	return render(request, 'registration/connexion.html', locals())


def deconnexion(request):

	logout(request)

	return redirect('http://localhost:8000/connexion/')

def inscription(request):

	if request.method == 'POST':

		form=InscriptionForm(request.POST or None)

		if form.is_valid():
			

			password = form.cleaned_data['password']
			pseudo = form.cleaned_data['pseudo']
			email = form.cleaned_data['email']
			user =User.objects.create_user(username = pseudo , email= email , password = password)
			Profil( user = user, avatar = 'avatar/default.jpg' ).save()

	else:
		form = InscriptionForm()


	return render(request, 'registration/inscription.html', locals())





@login_required
def mon_compte(request):


	return render(request, 'registration/mon_compte.html', locals())





def contact(request):



	form = ContactForm(request.POST or None)


	if form.is_valid(): 

		# Ici nous pouvons traiter les données du formulaire

		sujet = form.cleaned_data['sujet']
		message = form.cleaned_data['message']
		envoyeur = form.cleaned_data['envoyeur']
		renvoi = form.cleaned_data['renvoi']

		from django.core.mail import send_mail

		send_mail( sujet, message , 'chpoutgnouf@gmail.com', [envoyeur] , fail_silently=False)

		envoi = True


	return render(request, 'contact.html', locals())

def accueil(request):
	jeux = Jeu.objects.all() 
	genres = Genre.objects.all()

	return render(request, 'accueil.html', {'jeux': jeux, 'genres': genres })




class FAQView(TemplateView):
	
	template_name = "accueil.html"  # chemin vers le template à afficher

class ListeJeux(ListView):

	model = Jeu
	context_object_name="jeux"
	template_name = "guide.html"


def test(request):
	bim=range(0,43)
	part=[]
	
	for i in range(1,43):
		boum = "#id" + str(i) + "{ font-family: " + "'"+str(i) + "'" +";}"
		
		part.append(boum)

	return render(request, 'registration/supprimer/a.html', locals())


		