# Generated by Django 4.2.4 on 2024-02-23 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuserv2',
            name='projeto_proin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
