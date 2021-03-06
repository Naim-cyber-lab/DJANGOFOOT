# Generated by Django 3.2.3 on 2021-05-28 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Equipes', '0013_coachparams_player_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='coachparams',
            name='currentTeam',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Equipes.team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coachparams',
            name='team',
            field=models.ManyToManyField(blank=True, related_name='utilisateur', to='Equipes.Team'),
        ),
        migrations.AddField(
            model_name='coachparams',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='player',
            name='VMA',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='firstName',
            field=models.CharField(default=None, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='globalScore',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='heigth',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='lastName',
            field=models.CharField(default=None, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='placeOnField',
            field=models.CharField(default=None, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Equipes.team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='weight',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='attendance',
            field=models.CharField(default=None, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='teamName',
            field=models.CharField(default=None, max_length=256),
            preserve_default=False,
        ),
    ]
