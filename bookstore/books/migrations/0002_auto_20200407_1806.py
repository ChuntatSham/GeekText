# Generated by Django 2.2.11 on 2020-04-07 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]