from django.db import models
from datetime import datetime
from accueil.models import Categorie, Profil
from django.contrib.postgres.fields import ArrayField
import ast


# Create your models here.

from django.utils import timezone


class ListField(models.Field):
	


	def db_type(self, connection):
		return 'ListField'
	def __init__(self, *args, **kwargs):
		super(ListField, self).__init__(*args, **kwargs)

	def to_python(self, value):
		if not value:
			value = []

		if isinstance(value, list):
			return value

		return ast.literal_eval(value)

	def get_prep_value(self, value):
		if value is None:
			return value

		return str(value)

	def value_to_string(self, obj):
		value = self._get_val_from_obj(obj)
		return self.get_db_prep_value(value)


	# def db_type(self, connection):
	# 	return 'ListField'

	# def __init__(self, separator=",", *args, **kwargs):
	# 	self.separator = separator
	# 	super().__init__(*args, **kwargs)

	# def deconstruct(self):
	# 	name, path, args, kwargs = super().deconstruct()
	# 	# Only include kwarg if it's not the default
	# 	if self.separator != ",":
	# 		kwargs['separator'] = self.separator
	# 	return name, path, args, kwargs


class Article(models.Model):
	titre = models.CharField(max_length=100)
	auteur = models.CharField(max_length=42)
	date = models.DateTimeField(default=timezone.now, 
								verbose_name="Date de parution")
	contenu = models.TextField(null=True)
	slug = models.SlugField(max_length=100)
	categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
	jeu = models.ForeignKey('Jeu', on_delete=models.CASCADE)

	class Meta:
		verbose_name = "article"
		ordering = ['date']
	
	def __str__(self):
		
		return self.titre




class Jeu(models.Model):
	nom = models.CharField(max_length=60)
	datesortie = models.DateField( null=True, blank = True, verbose_name='date de sortie' )
	genre = models.ManyToManyField('Genre', blank = True )
	
	solo = models.BooleanField( default = False)
	multi = models.BooleanField( default = False)

	censure = models.IntegerField(null=True, blank = True )
	nomVO = models.CharField(max_length=60, null=True, blank = True  )
	developpeur = models.CharField(max_length=60, null=True, blank = True )
	editeur = models.CharField(max_length=60, null=True, blank = True )

	slug = models.SlugField(max_length=60)
	photo = models.ImageField(upload_to="photos/jeu")

	MissionsPrincipales = ListField()
	MissionsAnnexes = ListField()
	Trophees = ListField()
	Autres = ListField()






	

	class Meta:
		
		verbose_name ="jeu"
		verbose_name_plural = "jeux"
		
			



	def __str__(self):

		return self.nom






class Genre(models.Model):
	
	genre = models.CharField(max_length=30)



	def __str__(self):
		ordering = ('-genre.jeu__nom.count()',)

		return self.genre



class Commentaire(models.Model):
	
	pseudo = models.ForeignKey(Profil, on_delete=models.SET_NULL, null=True, blank=True)
	
	
	commentaire = models.TextField(null=False)
	date = models.DateTimeField( default=datetime.now,
								verbose_name="Date de parution")
	jeu = models.ForeignKey('Jeu', blank=True, null=True, on_delete=models.SET_NULL )
	article = models.ForeignKey('Article', null=True, blank=True, on_delete=models.SET_NULL)
	lien = models.URLField(blank=True)
	GarsSur=models.BooleanField(default=False)

	class Meta:
	
		ordering = ('date',)
			


		
	def __str__(self):

		return self.commentaire

		

