# Generated by Django 5.1.2 on 2024-11-14 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_pagecontent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagecontent',
            name='shipping_info',
        ),
        migrations.AddField(
            model_name='pagecontent',
            name='shipping_information',
            field=models.TextField(default='Shipping information not provided yet.'),
        ),
        migrations.AlterField(
            model_name='pagecontent',
            name='about_us',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='pagecontent',
            name='head_title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='pagecontent',
            name='order_now',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='pagecontent',
            name='sub_title',
            field=models.CharField(max_length=200),
        ),
    ]
