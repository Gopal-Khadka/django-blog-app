# Generated by Django 5.1.1 on 2024-09-17 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_alter_blogauthor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogauthor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_authors'),
        ),
    ]
