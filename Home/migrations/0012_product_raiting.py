# Generated by Django 4.1.1 on 2022-09-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0011_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='raiting',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
