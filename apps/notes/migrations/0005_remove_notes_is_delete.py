# Generated by Django 2.2.4 on 2019-09-22 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_notes_is_delete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='is_delete',
        ),
    ]
