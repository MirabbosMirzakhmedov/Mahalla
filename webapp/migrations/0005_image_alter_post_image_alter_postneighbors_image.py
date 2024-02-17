# Generated by Django 5.0.1 on 2024-02-17 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_postneighbors_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='posts/default.webp', upload_to='posts/'),
        ),
        migrations.AlterField(
            model_name='postneighbors',
            name='image',
            field=models.ImageField(default='posts/default.webp', upload_to='posts/'),
        ),
    ]
