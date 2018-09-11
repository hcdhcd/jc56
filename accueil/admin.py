from django.contrib import admin

from .models import Profil
	
class ProfilAdmin(admin.ModelAdmin):
	list_display = ('user', )

admin.site.register(Profil, ProfilAdmin)

