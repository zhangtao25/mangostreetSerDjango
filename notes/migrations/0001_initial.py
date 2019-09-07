# Generated by Django 2.2.4 on 2019-09-01 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('type', models.CharField(default='normal', max_length=50)),
                ('desc', models.CharField(max_length=50)),
                ('likes', models.IntegerField(default=0)),
                ('cover', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('collects', models.IntegerField(default=0)),
                ('images', models.CharField(max_length=50)),
                ('is_delete', models.BooleanField(default=False, max_length=2)),
            ],
            options={
                'db_table': 'notes',
            },
        ),
    ]