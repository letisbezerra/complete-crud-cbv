from django.db import models
from django.utils import timezone
from cpf_field.models import CPFField

class Cliente(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    cpf = CPFField('cpf', max_length=14, unique=True, blank=False, null=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    telefone = models.CharField(max_length=50, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    data_cadastro = models.DateTimeField(default=timezone.now)    
    data_alteracao = models.DateTimeField(auto_now_add=True)  
    foto = models.ImageField(upload_to='media/') 
    
 
    def publish(self):
        self.publish_date = timezone.now
        self.save()

    def __str__(self):
        return self.nome

