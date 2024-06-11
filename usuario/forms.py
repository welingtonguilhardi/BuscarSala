from django import forms
from .models import Dias

class DiasForm(forms.ModelForm):
    class Meta:
        model = Dias
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Obter os valores de 'dia' já existentes no banco de dados
        dias_existentes = Dias.objects.values_list('dia', flat=True)
        # Filtrar choices para remover os já existentes
        self.fields['dia'].choices = [
            choice for choice in Dias.DIAS_CHOICES if choice[0] not in dias_existentes
        ]
