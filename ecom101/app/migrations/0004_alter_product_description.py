# Generated by Django 5.0.3 on 2024-03-11 09:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_product_author_alter_product_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.CharField(blank=True, default="", max_length=500, null=True),
        ),
    ]
