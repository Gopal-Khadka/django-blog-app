# Generated by Django 5.1.1 on 2024-09-16 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_blogpost_published_alter_blogpost_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogauthor',
            old_name='author',
            new_name='user',
        ),
    ]
