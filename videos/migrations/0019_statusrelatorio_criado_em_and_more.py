# Generated by Django 4.2.4 on 2024-03-22 01:16

from django.db import migrations, models
import django.db.models.deletion
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0018_statusrelatorio'),
    ]

    operations = [
        migrations.AddField(
        model_name='statusrelatorio',
        name='criado_em',
        field=models.DateTimeField(auto_now_add=True, default=timezone.now),  # Adicione default=timezone.now
        preserve_default=False,
    ),
        migrations.AlterField(
            model_name='statusrelatorio',
            name='relatorio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_relatorios', to='videos.relatorio'),
        ),
        migrations.AlterUniqueTogether(
            name='statusrelatorio',
            unique_together={('relatorio', 'usuario')},
        ),
    ]
