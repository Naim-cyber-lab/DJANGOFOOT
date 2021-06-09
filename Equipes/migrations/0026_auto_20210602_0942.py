# Generated by Django 3.2.3 on 2021-06-02 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Equipes', '0025_rename_model_gamemodel_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamemodel',
            name='game',
        ),
        migrations.AddField(
            model_name='game',
            name='gameModel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Equipes.gamemodel'),
        ),
    ]