# Generated by Django 2.2.4 on 2019-10-13 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191013_0552'),
        ('notes', '0007_remove_note_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.User'),
            preserve_default=False,
        ),
    ]
