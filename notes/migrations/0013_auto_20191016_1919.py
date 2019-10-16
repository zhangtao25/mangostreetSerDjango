# Generated by Django 2.2.6 on 2019-10-16 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0012_collect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='note_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.Note'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
    ]