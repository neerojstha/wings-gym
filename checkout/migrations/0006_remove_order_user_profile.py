# Generated by Django 3.2.21 on 2023-10-22 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user_profile',
        ),
    ]
