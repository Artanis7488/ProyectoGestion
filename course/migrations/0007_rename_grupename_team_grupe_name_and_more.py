# Generated by Django 4.0.3 on 2022-04-23 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='grupename',
            new_name='grupe_name',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='grupenumber',
            new_name='grupe_number',
        ),
    ]
