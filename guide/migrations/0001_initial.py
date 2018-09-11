# Generated by Django 2.0.7 on 2018-07-12 16:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accueil', '0002_auto_20180709_0037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('auteur', models.CharField(max_length=42)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de parution')),
                ('contenu', models.TextField(null=True)),
                ('slug', models.SlugField(max_length=100)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.Categorie')),
            ],
            options={
                'verbose_name': 'article',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentaire', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de parution')),
                ('lien', models.URLField(blank=True)),
                ('GarsSur', models.BooleanField(default=False)),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='guide.Article')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Jeu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=60)),
                ('slug', models.SlugField(max_length=60)),
                ('photo', models.ImageField(upload_to='photos/jeu')),
            ],
            options={
                'verbose_name': 'jeu',
                'ordering': ('nom',),
            },
        ),
        migrations.AddField(
            model_name='commentaire',
            name='jeu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='guide.Jeu'),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='pseudo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accueil.Profil'),
        ),
        migrations.AddField(
            model_name='article',
            name='jeu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.Jeu'),
        ),
    ]