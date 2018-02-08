# Generated by Django 2.0.2 on 2018-02-08 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postlike',
            name='post',
        ),
        migrations.RemoveField(
            model_name='postlike',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='like_users',
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ManyToManyField(to='many_to_many.User'),
        ),
        migrations.DeleteModel(
            name='PostLike',
        ),
    ]
