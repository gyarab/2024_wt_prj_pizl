# Generated by Django 5.1.6 on 2025-05-16 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_obrazek'),
    ]

    operations = [
        migrations.AddField(
            model_name='pecivo',
            name='obrazek_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
