# Generated by Django 3.0.2 on 2020-01-10 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passandplay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='text',
            field=models.TextField(default=''),
        ),
    ]