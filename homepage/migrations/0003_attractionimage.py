# Generated by Django 5.1.2 on 2024-11-13 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_product_hover_image_alter_product_discount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttractionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='attraction_images/')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
