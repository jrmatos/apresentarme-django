# Generated by Django 3.1.4 on 2020-12-16 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('bio', models.TextField(max_length=300)),
                ('photoUrl', models.CharField(max_length=100)),
                ('instagramUrl', models.CharField(max_length=100)),
                ('facebookUrl', models.CharField(max_length=100)),
                ('youtubeUrl', models.CharField(max_length=100)),
            ],
        ),
    ]
