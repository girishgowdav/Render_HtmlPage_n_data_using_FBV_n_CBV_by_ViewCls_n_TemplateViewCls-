# Generated by Django 4.2.1 on 2023-08-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('age', models.IntegerField()),
                ('section', models.CharField(max_length=100)),
            ],
        ),
    ]
