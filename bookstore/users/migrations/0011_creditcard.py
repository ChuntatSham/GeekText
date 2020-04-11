# Generated by Django 2.2.11 on 2020-04-11 17:11

from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_address_address_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=16)),
                ('expiration_month', models.CharField(choices=[('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'), ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], default='05', max_length=2)),
                ('expiration_year', models.CharField(choices=[('01', '2020'), ('02', '2021'), ('03', '2022'), ('04', '2023'), ('05', '2024'), ('06', '2025'), ('07', '2026'), ('08', '2027'), ('09', '2028'), ('10', '2029'), ('11', '2030'), ('12', '2031'), ('13', '2032'), ('14', '2033'), ('15', '2034')], default='01', max_length=2)),
                ('security_code', models.IntegerField()),
                ('cardholder_name', models.CharField(max_length=100)),
                ('default', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(default=users.models.Profile, on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
            options={
                'verbose_name_plural': 'CCards',
            },
        ),
    ]
