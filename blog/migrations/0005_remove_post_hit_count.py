# Generated by Django 3.0.6 on 2020-06-08 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_hit_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='hit_count',
        ),
    ]
