# Generated by Django 5.0.1 on 2024-02-14 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_alter_business_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='category',
            field=models.CharField(blank=True, choices=[('drugs', 'Aptekalar'), ('restaurants', 'Restoranlar / Kafelar'), ('stores', "Do'konlar / Savdo Markazlari"), ('clothing_stores', "Kiyim do'konlari"), ('beauty_salons', "Go'zallik salonlari"), ('auto_services', 'Avtomobil xizmatlari'), ('banks', 'Banklar'), ('home_improvement', "Uy uchun do'konlar"), ('fitness_centers', 'Fitnes markazlari'), ('educational_institutions', "Ta'lim muassasalari"), ('agencies', 'Agentliklar / Boshqa'), ('clinics', 'Kasalxonalar / Klinikalar')], max_length=255, null=True),
        ),
    ]