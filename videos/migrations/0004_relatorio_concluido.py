# Generated by Django 4.2.4 on 2024-02-24 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_aula_assistida_alter_aula_link_da_aula_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatorio',
            name='concluido',
            field=models.BooleanField(default=False),
        ),
    ]
