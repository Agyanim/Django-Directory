# Generated by Django 5.1.6 on 2025-03-18 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postApp', '0002_alter_posts_options_alter_posts_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]
