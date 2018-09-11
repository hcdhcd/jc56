from django.contrib import admin
from .models import Article, Jeu, Categorie, Commentaire, Genre

class ArticleAdmin(admin.ModelAdmin):
	list_display   = ('jeu', 'titre', 'auteur', 'date', 'id')

	date_hierarchy = 'date'
	ordering       = ('date', )
	search_fields  = ('titre', 'contenu')

admin.site.register(Article, ArticleAdmin)


class JeuAdmin(admin.ModelAdmin):
	list_display = ('nom', 'photo', 'id')
	ordering = ('nom', )

admin.site.register(Jeu, JeuAdmin)


class GenreAdmin(admin.ModelAdmin):
	pass


admin.site.register(Genre, GenreAdmin)

class CommentaireAdmin(admin.ModelAdmin):
	list_display = ('jeu', 'article', 'pseudo', 'commentaire', 'date', 'id')
	ordering = ('-date', )

admin.site.register(Commentaire, CommentaireAdmin)

admin.site.register(Categorie)
# Register your models here.

