# Generated by Django 4.2.4 on 2024-03-26 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0021_statusrelatorio_criado_em'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relatorio',
            old_name='ano_do_relatorio',
            new_name='ano',
        ),
        migrations.RenameField(
            model_name='relatorio',
            old_name='descricao_do_relatorio',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='relatorio',
            old_name='link_do_relatorio',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='relatorio',
            old_name='mes_do_relatorio',
            new_name='mes',
        ),
        migrations.RenameField(
            model_name='relatorio',
            old_name='nome_do_relatorio',
            new_name='nome',
        ),
        migrations.RemoveField(
            model_name='customuserv2',
            name='turma',
        ),
        migrations.RemoveField(
            model_name='relatorio',
            name='concluido',
        ),
        migrations.RemoveField(
            model_name='relatorio',
            name='usuario_concluiu',
        ),
        migrations.RemoveField(
            model_name='statusrelatorio',
            name='criado_em',
        ),
        migrations.AlterField(
            model_name='statusrelatorio',
            name='relatorio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.relatorio'),
        ),
    ]
