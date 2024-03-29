# Generated by Django 5.0.1 on 2024-02-18 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_image_alter_post_image_alter_postneighbors_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='reklama/')),
                ('full_text', models.TextField()),
                ('expiration_date', models.DateTimeField()),
            ],
        ),
    ]
