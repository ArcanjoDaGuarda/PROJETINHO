# Generated by Django 4.2.4 on 2024-03-21 00:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0014_customuserv2_relatorios_concluidos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuserv2',
            name='relatorios_concluidos',
        ),
        migrations.AddField(
            model_name='relatorio',
            name='usuario_concluiu',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
