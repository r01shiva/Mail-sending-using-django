# Generated by Django 2.0.7 on 2019-01-21 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='mobileno',
            field=models.PositiveIntegerField(),
        ),
    ]
