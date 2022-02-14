from django.contrib import admin
from takipapp.models import uruntakip
 

 
class uruntakipAdmin(admin.ModelAdmin):
    search_fields = ['cargono']
    list_display = ['cargoname', 'cargono', 'status']



admin.site.register(uruntakip, uruntakipAdmin)