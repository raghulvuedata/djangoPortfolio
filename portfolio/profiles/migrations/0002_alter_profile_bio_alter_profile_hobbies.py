# Generated by Django 4.2.1 on 2023-05-29 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hobbies',
            field=models.TextField(default=''),
        ),
    ]
