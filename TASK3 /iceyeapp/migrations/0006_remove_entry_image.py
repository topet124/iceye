# Generated by Django 3.1.7 on 2021-09-25 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iceyeapp', '0005_entry_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='image',
        ),
    ]