# Generated by Django 5.1.6 on 2025-03-28 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outward_supply', '0006_alter_outward_invoice_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailer',
            name='total_sales',
            field=models.FloatField(default=0),
        ),
    ]
