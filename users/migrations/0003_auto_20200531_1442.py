# Generated by Django 3.0.6 on 2020-05-31 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200528_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='3&D_main.png', upload_to='profile_pics'),
        ),
    ]