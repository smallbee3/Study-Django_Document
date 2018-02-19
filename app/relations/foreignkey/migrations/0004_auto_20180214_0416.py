# Generated by Django 2.0.2 on 2018-02-13 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foreignkey', '0003_auto_20180214_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foreignkey.Manufacturer', verbose_name='제조사'),
        ),
    ]