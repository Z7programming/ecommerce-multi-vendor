# Generated by Django 4.1.1 on 2022-09-11 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('titel', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='categories/logo/')),
                ('show_in_store', models.BooleanField(blank=True, default=True, null=True)),
                ('meta_titel', models.CharField(blank=True, default=models.CharField(blank=True, default='', max_length=100, null=True), max_length=100, null=True)),
                ('meta_description', models.TextField(blank=True, default=models.TextField(blank=True, default='', null=True), null=True)),
            ],
        ),
    ]
