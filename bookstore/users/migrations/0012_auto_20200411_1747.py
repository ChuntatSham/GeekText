# Generated by Django 2.2.11 on 2020-04-11 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_creditcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='expiration_year',
            field=models.CharField(choices=[('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030'), ('2031', '2031'), ('2032', '2032'), ('2033', '2033'), ('2034', '2034')], default='01', max_length=4),
        ),
    ]
