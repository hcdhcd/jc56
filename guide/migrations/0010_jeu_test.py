# Generated by Django 2.1 on 2018-09-04 16:47

from django.db import migrations
import guide.models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0009_auto_20180904_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='jeu',
            name='test',
            field=guide.models.ListField(default=1),
            preserve_default=False,
        ),
    ]
