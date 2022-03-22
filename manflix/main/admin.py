from django.contrib import admin
from .models import *

class detFilmes(admin.ModelAdmin):
    list_display = ('id','nome', 'categoria_fk')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Filmes, detFilmes)

class detCategoria(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Categoria, detCategoria)


class detAssinatura(admin.ModelAdmin):
    list_display = ('id','nome','valor')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Assinatura, detAssinatura)

class detUsuario(admin.ModelAdmin):
    list_display = ('id','nome','email','fone','status','assinatura_fk')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Usuario, detUsuario)

class detFavoritos(admin.ModelAdmin):
    list_display = ('id','filmes_fk','usuario_fk')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Favoritos, detFavoritos)
