# Generated by Django 2.0.1 on 2018-04-05 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upvote',
            field=models.IntegerField(default=0),
        ),
    ]
