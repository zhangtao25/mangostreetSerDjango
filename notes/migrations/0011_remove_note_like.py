# Generated by Django 2.2.4 on 2019-10-13 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0010_note_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='like',
        ),
    ]