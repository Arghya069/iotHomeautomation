# Generated by Django 3.0.2 on 2021-11-20 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raspi', '0004_auto_20211118_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledstat',
            name='temprature',
            field=models.FloatField(default=0.0),
        ),
    ]