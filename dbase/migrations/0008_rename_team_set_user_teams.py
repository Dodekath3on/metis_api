# Generated by Django 4.2.4 on 2024-01-27 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbase', '0007_user_team_set'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='team_set',
            new_name='teams',
        ),
    ]