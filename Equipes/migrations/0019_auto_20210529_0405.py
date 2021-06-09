# Generated by Django 3.2.3 on 2021-05-29 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Equipes', '0018_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='game',
        ),
        migrations.AddField(
            model_name='group',
            name='player',
            field=models.ManyToManyField(blank=True, related_name='groups', to='Equipes.Player'),
        ),
    ]
