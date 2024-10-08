# Generated by Django 5.1.1 on 2024-09-17 05:02

import easy_thumbnails.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_alter_blogpost_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogauthor',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='blog_authors'),
        ),
    ]
