# Generated by Django 2.0.2 on 2018-03-08 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='COMMENT',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='DATE',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='NICKNAME',
            new_name='nickname',
        ),
    ]
