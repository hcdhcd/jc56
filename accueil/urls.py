from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views
from guide.models import Jeu
from django.views.generic import ListView



urlpatterns = [

	path('contact', views.contact, name='contact'),
	path('', views.accueil, name='accueil'),
	path('connexion/', views.connexion, name='connexion'),
	path('deconnexion', views.deconnexion, name='deconnexion'),
	path('inscription', views.inscription, name='inscription'),
	path('mon_compte/', views.mon_compte, name="mon_compte"),
	path('test', views.test),
	re_path(r'^faq$', views.FAQView.as_view() ), # Nous demandons la vue correspondant à la classe FAQView)
	

]