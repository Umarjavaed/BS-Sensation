# Generated by Django 5.1.2 on 2024-11-13 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_attractionimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attractionimage',
            name='title',
            field=models.CharField(blank=True, default='Default Title', max_length=255),
            preserve_default=False,
        ),
    ]
