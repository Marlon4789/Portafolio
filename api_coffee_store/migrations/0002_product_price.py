# Generated by Django 5.0.2 on 2024-03-07 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_coffee_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
