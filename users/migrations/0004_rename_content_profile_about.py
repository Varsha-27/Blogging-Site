# Generated by Django 4.0.1 on 2022-02-01 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='content',
            new_name='about',
        ),
    ]