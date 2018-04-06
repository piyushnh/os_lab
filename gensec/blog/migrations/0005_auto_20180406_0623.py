# Generated by Django 2.0.1 on 2018-04-06 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180406_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secretary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='blog.Comment'),
        ),
        migrations.AddField(
            model_name='secretary',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Comment'),
        ),
    ]