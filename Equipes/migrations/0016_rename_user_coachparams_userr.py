# Generated by Django 3.2.3 on 2021-05-28 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Equipes', '0015_alter_coachparams_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coachparams',
            old_name='user',
            new_name='userr',
        ),
    ]
