from django.http import Http404, HttpRequest
from .models import Profil
from guide.models import Jeu


def get_infos(request):

	user_profil= None
	jeux = Jeu.objects.all() 

	if request.user.is_authenticated:
		user_profil= Profil.objects.get( user = request.user )

	return {'user_profil': user_profil, 'jeux': jeux }
	
