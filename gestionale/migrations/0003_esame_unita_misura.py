# Generated by Django 4.2.6 on 2023-11-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionale', '0002_paziente_esame_paziente'),
    ]

    operations = [
        migrations.AddField(
            model_name='esame',
            name='unita_misura',
            field=models.CharField(max_length=20, null=True),
        ),
    ]