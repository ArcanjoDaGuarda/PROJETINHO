# Generated by Django 4.2.4 on 2024-03-20 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_rename_data_aula_data_da_aula_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='assistida',
            field=models.BooleanField(default=False),
        ),
    ]
