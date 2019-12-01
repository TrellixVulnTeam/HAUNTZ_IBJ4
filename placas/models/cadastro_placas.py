from django.db import models

# Create your models here.class Menu_placas(models.Model):
class Cadastro_placas(models.Model):
    Numero_serie = models.CharField(
        'Número de série',
        max_length=120,
        unique=True
    )
    
    Modelo = models.ForeignKey(
        'placas.modelo_placas', 
        related_name='modelo_placas_modelo',
        on_delete = models.PROTECT,
        null = True,
        limit_choices_to= {'Ativo': True} #Limita somente a modelos ativos
    )

    Revisao_lm = models.IntegerField(
        'Revisao LM'
    )

    Lote_numero = models.ForeignKey(
            'placas.cadastro_lote',
            related_name='Lote_numero_lote',
            on_delete = models.PROTECT,
            null=True,
            limit_choices_to= {'Ativo': True} #Limita somente a modelos ativos
        )

    Observacao = models.TextField(
        'Observação',
        blank=True
    )

    Ativo = models.BooleanField(
        'Placa Ativa',
        default=True
    )
    
    def __str__(self):
        return '{} - {}'.format(self.Numero_serie, self.Modelo)

    class Meta:
        db_table = 'CADASTRO_PLACAS'
        constraints = [
            models.UniqueConstraint(fields=['Numero_serie'], name="Constraint_placas")
        ]



