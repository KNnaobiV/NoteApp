# Generated by Django 3.2.5 on 2021-07-23 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
