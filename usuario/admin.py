# admin.py

from django.contrib import admin
from .models import Sala, Curso, RegistroCurso,AtivarPesquisaSalas
from django.contrib.auth.models import User, Group

from django.core.exceptions import ValidationError



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
    
class AtivarPesquisaSalasAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Impedir a adição de novos registros se já houver um existente
        if AtivarPesquisaSalas.objects.exists():
            return False
        return super().has_add_permission(request)
    
    def save_model(self, request, obj, form, change):
        if not change and AtivarPesquisaSalas.objects.exists():
            raise ValidationError('Já existe um registro de AtivarPesquisaSalas.')
        super().save_model(request, obj, form, change)

admin.site.register(AtivarPesquisaSalas, AtivarPesquisaSalasAdmin)
admin.site.register(Sala, SalaAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(RegistroCurso, RegistroCursoAdmin)
