# Generated by Django 5.1.1 on 2024-12-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_cuser_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuser',
            name='user_profile',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic'),
        ),
    ]