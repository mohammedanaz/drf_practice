# Generated by Django 5.0.7 on 2024-07-31 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='store',
            new_name='book',
        ),
    ]
