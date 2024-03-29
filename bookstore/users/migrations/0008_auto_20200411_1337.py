# Generated by Django 2.2.11 on 2020-04-11 13:37

from django.db import migrations, models
import django_countries.fields
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address_type',
            field=models.CharField(choices=[('B', 'Billing'), ('S', 'Shipping')], default='B', max_length=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='apartment_address',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=django_countries.fields.CountryField(default='US', max_length=2),
        ),
        migrations.AddField(
            model_name='profile',
            name='default',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='street_address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='zip',
            field=models.IntegerField(default=0, validators=[users.models.validate_zip]),
        ),
    ]
