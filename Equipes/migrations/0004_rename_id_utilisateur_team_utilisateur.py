# Generated by Django 3.2.3 on 2021-05-26 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Equipes', '0003_auto_20210526_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='id_utilisateur',
            new_name='utilisateur',
        ),
    ]
