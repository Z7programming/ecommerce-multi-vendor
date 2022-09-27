# Generated by Django 4.1.1 on 2022-09-23 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_remove_category_baner'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_titel',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_titel',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]