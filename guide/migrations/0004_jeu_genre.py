# Generated by Django 2.0.7 on 2018-07-16 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0003_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='jeu',
            name='genre',
            field=models.ManyToManyField(to='guide.Genre'),
        ),
    ]
