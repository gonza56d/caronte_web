# Generated by Django 3.1.7 on 2021-03-28 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailies', '0003_auto_20210328_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9),
        ),
    ]
