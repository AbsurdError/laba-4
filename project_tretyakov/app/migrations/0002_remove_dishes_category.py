# Generated by Django 4.2.7 on 2023-12-20 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dishes',
            name='category',
        ),
    ]