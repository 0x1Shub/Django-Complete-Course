# Generated by Django 5.1.7 on 2025-03-28 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_address_zip'),
    ]

    operations = [
        migrations.RunSQL(""" INSERT INTO store_collection (title)  """)
    ]
