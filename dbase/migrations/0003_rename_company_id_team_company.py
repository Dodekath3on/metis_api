# Generated by Django 4.2.4 on 2024-01-25 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbase', '0002_company_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='company_id',
            new_name='company',
        ),
    ]
