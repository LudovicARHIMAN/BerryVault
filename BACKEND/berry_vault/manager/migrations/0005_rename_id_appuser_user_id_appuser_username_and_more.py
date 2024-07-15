# Generated by Django 5.0.7 on 2024-07-15 19:34

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_rename_user_id_appuser_id_remove_appuser_username_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appuser',
            old_name='id',
            new_name='user_id',
        ),
        migrations.AddField(
            model_name='appuser',
            name='username',
            field=models.CharField(default=uuid.uuid4, max_length=50),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
    ]
