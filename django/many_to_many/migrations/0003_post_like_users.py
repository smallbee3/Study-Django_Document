# Generated by Django 2.0.2 on 2018-02-05 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0002_auto_20180205_0700'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_users',
            field=models.ManyToManyField(through='many_to_many.PostLike', to='many_to_many.User'),
        ),
    ]
