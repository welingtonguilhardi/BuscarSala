# admin.py

from django.contrib import admin
from .models import Sala, Curso, RegistroCurso
from django.contrib.auth.models import User, Group


# Removendo os modelos User e Group do painel de administração
admin.site.unregister(User)
admin.site.unregister(Group)

class SalaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'pavilhao')
    list_filter = ('pavilhao','numero')
    search_fields = ('numero', 'url')
    search_help_text = 'Busque aqui por numero da sala.'

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    search_help_text = 'Busque aqui por nome do curso.'

class RegistroCursoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'semestre', 'turno', 'sala')
    list_filter = ('turno', 'semestre', 'curso', 'sala')
    search_fields = ('curso__nome', 'sala__numero')
    search_help_text = 'Busque aqui por numero da sala ou nome do curso.'

admin.site.register(Sala, SalaAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(RegistroCurso, RegistroCursoAdmin)
