# Generated by Django 4.0.4 on 2022-05-05 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raterprojectapi', '0002_rename_user_id_gamer_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='game_id',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='gamer_id',
            new_name='gamer',
        ),
    ]
