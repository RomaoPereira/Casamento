from django.db import models

class Guest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('confirmed', 'Confirmado'),
        ('declined', 'Não irá'),
    ]

    name = models.CharField(max_length=200, verbose_name="Nome do Convidado/Família")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Status da Confirmação")
    
    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"
    
    class Meta:
        verbose_name = "Convidado"
        verbose_name_plural = "Convidados"

class Gift(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome do Presente")
    is_chosen = models.BooleanField(default=False, verbose_name="Já foi escolhido?")

    def __str__(self):
        return f"{self.name} - {'(Escolhido)' if self.is_chosen else '(Disponível)'}"
    
    class Meta:
        verbose_name = "Presente"
        verbose_name_plural = "Lista de Presentes"
