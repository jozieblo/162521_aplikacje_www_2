# Generated by Django 4.2.7 on 2023-11-23 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_alter_osoba_nazwisko'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='osoba',
            name='imie',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='osoba',
            name='nazwisko',
            field=models.CharField(max_length=70),
        ),
    ]
