# Generated by Django 5.1.1 on 2024-09-17 00:51

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_rename_author_blogauthor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
