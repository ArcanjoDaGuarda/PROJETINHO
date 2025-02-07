# Generated by Django 4.2.4 on 2024-03-14 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0009_rename_data_da_aula_aula_data_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aula',
            old_name='data',
            new_name='data_da_aula',
        ),
        migrations.RenameField(
            model_name='aula',
            old_name='link_aula',
            new_name='link_da_aula',
        ),
        migrations.RenameField(
            model_name='aula',
            old_name='link_gravacao',
            new_name='link_da_gravacao',
        ),
        migrations.RenameField(
            model_name='aula',
            old_name='link_inscricao',
            new_name='link_da_inscricao',
        ),
        migrations.RemoveField(
            model_name='aula',
            name='nome',
        ),
        migrations.AddField(
            model_name='aula',
            name='nome_da_aula',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aula',
            name='palestrante',
            field=models.CharField(max_length=255),
        ),
    ]
