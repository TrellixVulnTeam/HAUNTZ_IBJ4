# Generated by Django 2.2.4 on 2019-12-01 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testes', '0010_auto_20191129_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teste',
            name='Descricao',
        ),
        migrations.AlterField(
            model_name='teste',
            name='Lote_numero',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Número de Lote'),
        ),
        migrations.AlterField(
            model_name='teste',
            name='Situacao',
            field=models.CharField(choices=[('Aprovado', 'Aprovado'), ('Reprovado', 'Reprovado')], max_length=20, verbose_name='Situação do teste'),
        ),
        migrations.AlterField(
            model_name='teste',
            name='Status',
            field=models.CharField(blank=True, choices=[('Pendente', 'Pendente'), ('Em andamento', 'Em andamento'), ('Finalizado', 'Finalizado')], max_length=20, verbose_name='Status do Teste'),
        ),
    ]
