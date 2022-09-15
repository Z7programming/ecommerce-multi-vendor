# Generated by Django 4.1.1 on 2022-09-13 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='State',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='Street',
            new_name='street',
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='', upload_to='profiles'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sall_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
