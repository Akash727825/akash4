# Generated by Django 5.0.6 on 2024-06-20 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_rename_customar_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]