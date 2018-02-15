# Generated by Django 2.0.2 on 2018-02-11 05:23

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0007_auto_20180211_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('proxy.user',),
            managers=[
                ('secondary', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('proxy.user',),
            managers=[
                ('secondary', django.db.models.manager.Manager()),
            ],
        ),
    ]
