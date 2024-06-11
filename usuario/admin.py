# admin.py

from django.contrib import admin
from .models import Contador, Sala, Curso, RegistroCurso,AtivarPesquisaSalas,CronogramaSala,Dias
from django.contrib.auth.models import User, Group
from .forms import DiasForm
from django.db.models import Count



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

class CronogramaSalaInline(admin.TabularInline):  # ou admin.StackedInline
    model = RegistroCurso.sala.through
    extra = 1

class RegistroCursoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'semestre', 'turno')
    list_filter = ('turno', 'semestre', 'curso', 'sala')
    search_fields = ('curso__nome', 'sala__numero')
    search_help_text = 'Busque aqui por numero da sala ou nome do curso.'
    inlines = [CronogramaSalaInline]
    
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
admin.site.register(CronogramaSala)

class DiasAdmin(admin.ModelAdmin):
    form = DiasForm

admin.site.register(Dias, DiasAdmin)


class ContadorAdmin(admin.ModelAdmin):
    list_display = ('sala', 'data')
    list_filter = ('sala', 'data')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(sala_count=Count('sala'))
        return qs

    def sala_count(self, obj):
        return obj.sala_count

admin.site.register(Contador, ContadorAdmin)
