# Generated by Django 3.2.5 on 2021-11-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LedStat',
            fields=[
                ('device_id', models.TextField(max_length=10, primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(0, 0), (1, 1)])),
            ],
        ),
    ]
