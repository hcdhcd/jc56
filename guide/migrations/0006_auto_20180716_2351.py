# Generated by Django 2.0.7 on 2018-07-16 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0005_auto_20180716_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jeu',
            name='genre',
            field=models.ManyToManyField(to='guide.Genre'),
        ),
    ]
