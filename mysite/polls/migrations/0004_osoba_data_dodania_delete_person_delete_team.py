# Generated by Django 4.2.7 on 2023-11-22 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_stanowisko_osoba'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
