from django.urls import path, re_path
from . import views
from django.shortcuts import render, redirect



urlpatterns = [

	path('', views.guide, name='guide'),
	
	#re_path(r'^([\w-]+)/([\w-]+)$', views.redirectTemplate, name='redirect template'),

	re_path(r'^(?P<slug_jeu>[\w-]+)/(?P<slug_article>[\w-]+)$', views.ArticleVue, name ='ArticleVue'),
	re_path(r'^(?P<slug_jeu>[\w-]+)', views.JeuSommaire, name ='JeuSommaire'),
	
	path('login', views.login),
	#path('<slug:slug_jeu>/<slug:slug_article>', views.redirectTemplate, name ='redirect template')


	

]
