# Generated by Django 5.1.1 on 2024-09-15 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blogpost_image_alter_blogauthor_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogauthor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_authors'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blogs'),
        ),
    ]