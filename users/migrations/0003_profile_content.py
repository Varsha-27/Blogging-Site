# Generated by Django 4.0.1 on 2022-02-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_user_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
