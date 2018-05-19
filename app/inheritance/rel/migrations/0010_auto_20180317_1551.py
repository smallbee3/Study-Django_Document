# Generated by Django 2.0.2 on 2018-03-17 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rel', '0009_auto_20180311_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_foods', related_query_name='item', to='rel.Person'),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_fruits', related_query_name='item', to='rel.Person'),
        ),
    ]