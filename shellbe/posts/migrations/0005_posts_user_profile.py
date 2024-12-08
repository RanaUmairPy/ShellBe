# Generated by Django 5.1.1 on 2024-12-08 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_posts_user_profile'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='user_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='users.usercreate'),
        ),
    ]