# Generated by Django 3.1.7 on 2021-03-11 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily',
            name='expense',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='daily',
            name='remainder',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
    ]