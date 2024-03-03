from django.contrib import admin
from aplicacao.models import Postagem

class Postagens(admin.ModelAdmin):
    list_display = ('id','username', 'title', 'content', 'created_datetime')
    list_display_links = ('id', 'username')
    search_fields = ('username',)
    list_per_page = 20

admin.site.register(Postagem, Postagens)
