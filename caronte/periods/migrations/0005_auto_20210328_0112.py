# Generated by Django 3.1.7 on 2021-03-28 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('periods', '0004_period_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]
