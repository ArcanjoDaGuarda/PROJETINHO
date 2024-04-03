from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nome} - {self.ano}"

class Relatorio(models.Model):
    nome = models.CharField(max_length=100)
    mes = models.CharField(max_length=20)
    ano = models.IntegerField()
    descricao = models.TextField()
    link = models.URLField(max_length=400)

class CustomUserV2(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    projeto_proin = models.CharField(max_length=100, blank=True, null=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='alunos', null=True, blank=True)
    relatorios_concluidos = models.ManyToManyField('Relatorio', related_name='usuarios_concluidos', blank=True)
    aulas_concluidas = models.ManyToManyField('Aula', related_name='usuarios_concluidos', blank=True)

    @property
    def Nome_Turma(self):
        if self.turma:
            return self.turma.nome 
        else:
            return "Sem turma associada"

class StatusRelatorio(models.Model):
    relatorio = models.ForeignKey(Relatorio, on_delete=models.CASCADE)
    usuario = models.ForeignKey(CustomUserV2, on_delete=models.CASCADE)
    concluido = models.BooleanField(default=False)

    class Meta:
        unique_together = ('relatorio', 'usuario')
    

class Aula(models.Model):
    nome_da_aula = models.CharField(max_length=255)
    palestrante = models.CharField(max_length=255)
    data_da_aula = models.DateField()
    descricao = models.TextField()
    link_da_aula = models.URLField()
    link_da_gravacao = models.URLField()
    link_da_inscricao = models.URLField()
    assistida = models.BooleanField(default=False)

    def is_completed_by(self, usuario):
        try:
            status_aula = StatusAula.objects.get(aula=self, usuario=usuario)
            return status_aula.assistida
        except StatusAula.DoesNotExist:
            return False

class StatusAula(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    usuario = models.ForeignKey(CustomUserV2, on_delete=models.CASCADE)
    assistida = models.BooleanField(default=False)
    data_conclusao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aula.nome_da_aula} - {self.usuario.username} - Concluída: {self.assistida}"


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
