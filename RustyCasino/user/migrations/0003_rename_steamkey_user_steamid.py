# Generated by Django 3.2.8 on 2021-11-02 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_users_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='steamKey',
            new_name='steamId',
        ),
    ]