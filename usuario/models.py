from django.db import models

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
    
class RegistroCurso(models.Model):
    
    TURNO_CHOICES = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite')
    ]
    
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    semestre = models.IntegerField()
    turno = models.CharField(max_length=5, choices=TURNO_CHOICES)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    



