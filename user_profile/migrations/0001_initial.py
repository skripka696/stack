# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 13:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=50, null=True)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, default='user/avatar/photo.jpg', null=True, upload_to='user/avatar')),
                ('place_of_activity', models.CharField(max_length=100)),
                ('form', models.CharField(choices=[('W', 'work'), ('S', 'study')], default='S', max_length=255)),
                ('rating', models.IntegerField()),
                ('skill', models.ManyToManyField(to='tag.Tag')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]