# Generated by Django 4.2.5 on 2023-10-10 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_certificates_faculty_advisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificates',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]