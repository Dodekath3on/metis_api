# Generated by Django 4.2.4 on 2024-01-27 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbase', '0005_user_projects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='projects',
            new_name='project_set',
        ),
    ]