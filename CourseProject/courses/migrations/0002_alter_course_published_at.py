# Generated by Django 4.2.11 on 2024-04-20 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='published_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]