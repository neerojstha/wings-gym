# Generated by Django 3.2.21 on 2023-10-22 00:00

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=models.CASCADE, to='auth.User')),
                # Add other fields for the UserProfile model here.
            ],
        ),
    ]
