# Generated by Django 2.2.4 on 2019-09-16 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Replys',
            fields=[
                ('reply_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=50)),
                ('reply_user_id', models.CharField(max_length=50)),
                ('comment_id', models.CharField(max_length=50)),
                ('reply_content', models.CharField(max_length=50)),
                ('createtime', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'replys',
            },
        ),
    ]