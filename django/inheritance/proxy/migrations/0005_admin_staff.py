# Generated by Django 2.0.2 on 2018-02-11 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0004_auto_20180211_1201'),
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
        ),
    ]
