# Generated by Django 4.1.1 on 2022-09-11 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_category_meta_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('titel', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='products/images/')),
                ('show_in_store', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('meta_titel', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('meta_description', models.TextField(blank=True, default='', null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.category')),
            ],
        ),
    ]
