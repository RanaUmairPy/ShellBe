# Generated by Django 5.1.1 on 2024-12-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuser',
            name='user_profile',
            field=models.ImageField(default=1, upload_to='profile_pic'),
            preserve_default=False,
        ),
    ]