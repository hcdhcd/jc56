from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, unique = True)
	avatar = models.ImageField(null=True, blank=True, upload_to = 'avatars/')
	signature = models.TextField(blank = True, null=True)
	inscrit_newsletter = models.BooleanField(default = False)

	def __str__(self):
		return self.user.username


class Categorie(models.Model):
	nom = models.CharField(max_length=30)

	def __str__(self):
		return self.nom



