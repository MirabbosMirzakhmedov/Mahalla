# Generated by Django 5.0.1 on 2024-02-12 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='../../media/posts/default.webp', upload_to='posts/'),
        ),
    ]
