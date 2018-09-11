from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from datetime import date, time, datetime
from guide.models import Article, Jeu, Commentaire, Genre
from accueil.models import Profil
from django.db.models.functions import Substr
from guide.forms import CommentaireForm, JeuForm
import os


def guide(request) :
	


	
	
	form = JeuForm(request.GET)
	if form.is_valid() : 
		r =  form.cleaned_data
		result = list()
		resultbis = list()
		jeux = Jeu.objects.filter(nom__icontains = r['nom'])
		jeuxv = Jeu.objects.filter( nomVO__icontains = r['nom'])
	


		if r['solo'] : 
			jeuxs = Jeu.objects.filter(solo = True)
		else :
			jeuxs = jeux
		if r['multi'] : 
			jeuxm = Jeu.objects.filter(multi = True)
		else : 
			jeuxm = jeux
		if r['censure'] : 
			jeuxc = Jeu.objects.filter( censure__lte = r['censure'])
		else : 
			jeuxc = jeux
		if r['developpeur'] :
			jeuxd = Jeu.objects.filter( developpeur__icontains = r['developpeur'])
		else : 
			jeuxd = jeux
		if r['editeur'] :
			jeuxd = Jeu.objects.filter( developpeur__icontains = r['editeur'])
		else : 
			jeuxe = jeux

	jeux= jeux.union(jeuxv).intersection(jeuxs, jeuxm, jeuxc, jeuxd, jeuxe).order_by('nom')


		# r['nom'] = None
		# for entry in r :
		# 	if r[entry] :
				
		# 		variable_column = entry
		# 		search_type = 'icontains'
		# 		dam = variable_column + '__' + search_type
		# 		jeux=jeux.filter(**{ dam: r[entry] })

				
		# 		result.append(r[entry])
		# 		resultbis.append(entry)

			# jeux = Jeu.objects.filter(nom__icontains = "" )
			# jeuxvo = Jeu.objects.filter(nomVO__icontains = "")
			# jeux = jeux.union(jeuxvo)


	return render (request,'guide.html', {'jeux': jeux, 'form' : form, 'resultform' : r['developpeur'] })



def JeuSommaire(request, slug_jeu ) :

	slug = slug_jeu + ".html"

	return render(request, 'JeuSommaire.html', locals())



def ArticleVue(request, slug_jeu, slug_article ) :

	slug = slug_jeu + "/" + slug_article + ".html"
	jeu= Jeu.objects.get( slug = slug_jeu)

	form = CommentaireForm(request.POST or None)

	if form.is_valid():
		complete = form.save(commit=False)
		complete.date= datetime.now()
		complete.lien= request.META['HTTP_REFERER']
		complete.jeu = jeu
		complete.article = Article.objects.get(slug = slug_article)

		if request.user.is_authenticated:
			complete.pseudo= Profil.objects.get(user = request.user )
			complete.save()

			form = CommentaireForm()
		
		else :
			anonyme= User.objects.get(username='Anonyme')
			complete.pseudo= Profil.objects.get(user = anonyme )
			complete.save()

			form = CommentaireForm()

	#Affichage des commentaires
	lien='http://localhost:8000/guide/'+ slug_jeu+'/'+ slug_article
	commentaires = Commentaire.objects.filter( lien = lien)

	#Editer commentaire
	if request.POST.get('comm_id') :
		com_id =int( request.POST['comm_id'] )

		if request.POST.get('edition_commentaire') :
			
			comment_edited = Commentaire.objects.get(	id = com_id	)
			comment_edited.commentaire = request.POST['edition_commentaire']
			comment_edited.save()
			
		
			com_id =None
			comment_edited = None



	if request.POST.get('delete_comm_id'):
		Commentaire.objects.get(	id = int(request.POST['delete_comm_id'])	).delete()



	return render(request, 'article.html', locals()) 


def login(request) :

	if len(request.POST):

		if'email' not in request.POST or 'password' not in request.POST:
			error = 'Veuillez entrer une addresse de courriel'
			return render(request, 'login.html', {'error': error})
		else:
			email = request.POST['email']
			password = request.POST['password']

			if 'password' !='kakaki' or email!='jc56@gmail.com':
				error='adresse email ou mot de passe incorrect'
				return render(request, 'login.html', {'error': error})
			else:
				return redirect('http://localhost:8000/guide/bienvenue')
	else: return render(request, 'login.html')

def comment(request) :

	slug = os.path.split(os.path.split(request.path)[0])[1]+ '/' + os.path.split(request.path)[1] + '.html'
	form = CommentaireForm(request.POST or None)

	if form.is_valid(): 

		pseudo = form.cleaned_data['pseudo']
		sujet = form.cleaned_data['sujet']
		commentaire = form.cleaned_data['commentaire']
		form.article= os.path.split(request.path)[1]
		form.jeu = os.path.split(os.path.split(request.path)[0])[1]

		envoi = True
		form.save()


	return form



