# Generated by Django 5.0.5 on 2024-05-28 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempuser',
            name='age',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]