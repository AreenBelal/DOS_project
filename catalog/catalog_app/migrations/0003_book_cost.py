# Generated by Django 4.2.7 on 2023-11-09 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0002_book_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cost',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
