# Generated by Django 4.2.1 on 2023-05-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('skills', models.CharField(max_length=200)),
                ('profile_picture', models.ImageField(upload_to='profile_pictures')),
                ('work_experience', models.TextField()),
                ('hobbies', models.TextField()),
            ],
        ),
    ]