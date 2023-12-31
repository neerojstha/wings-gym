# Generated by Django 3.2.23 on 2024-01-07 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20231231_0136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='featured_image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=210, unique=True),
        ),
    ]
