# Generated by Django 3.2.3 on 2021-05-26 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Equipes', '0007_auto_20210526_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateur',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='lastName',
        ),
    ]