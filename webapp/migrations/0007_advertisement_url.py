# Generated by Django 5.0.1 on 2024-02-18 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_advertisement'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='url',
            field=models.URLField(default='https://yandex.com/maps/-/CDBwVA-a'),
        ),
    ]
