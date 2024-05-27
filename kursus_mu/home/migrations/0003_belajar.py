# Generated by Django 4.2.13 on 2024-05-25 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_siswa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Belajar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('status', models.BooleanField()),
                ('link', models.TextField()),
                ('kursus', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='home.kursus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]