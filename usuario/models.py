from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

class Curso (models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome

class Sala (models.Model):
    PAVILHAO_CHOICES = [
        ('1', 'Pavilhão 01'),
        ('2', 'Pavilhão 02'),
    ]

    pavilhao = models.CharField(max_length=1,choices=PAVILHAO_CHOICES)    
    numero = models.IntegerField()
    url = models.CharField(max_length=250)
    
    def __str__(self) :
        return f'Sala N°{self.numero} | Pavilhão N° {self.pavilhao}'
    
class Dias (models.Model):
    
    DIAS_CHOICES = [
        ('1','Domingo'),
        ('2', 'Segunda Feira'),
        ('3', 'Terça Feira'),
        ('4', 'Quarta Feira'),
        ('5','Quinta Feira'),
        ('6', 'Sexta Feira'),
        ('7', 'Sábado'),
    ]
    
    dia = models.CharField(max_length=1,choices=DIAS_CHOICES)
    
    def __str__(self) -> str:
        return self.get_dia_display()
    
    def get_number_day(self):
        return self.dia
class CronogramaSala (models.Model):
    
    dias = models.ManyToManyField(Dias)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    
    def __str__(self) :
        # Obter os nomes dos dias
        nomes_dias = ', '.join([dia.get_dia_display() for dia in self.dias.all()])
        return f'{nomes_dias} | {self.sala}'
class RegistroCurso(models.Model):
    
    TURNO_CHOICES = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite')
    ]
    
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    semestre = models.IntegerField()
    turno = models.CharField(max_length=5, choices=TURNO_CHOICES)
    sala = models.ManyToManyField(CronogramaSala)
    
class AtivarPesquisaSalas(models.Model):
    ativado = models.BooleanField(default=False)

    def __str__(self):
        return "Pesquisa de Salas Ativada" if self.ativado else "Pesquisa de Salas Desativada"
    

    def save(self, *args, **kwargs):
        if not self.pk and AtivarPesquisaSalas.objects.exists():
            raise ValidationError('Já existe um registro de AtivarPesquisaSalas.')
        super(AtivarPesquisaSalas, self).save(*args, **kwargs)

class Contador (models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.sala} em {self.data.strftime("%Y-%m-%d %H:%M:%S")}'