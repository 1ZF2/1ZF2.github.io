# Generated by Django 4.1.7 on 2023-05-07 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(name="Link",),
    ]
