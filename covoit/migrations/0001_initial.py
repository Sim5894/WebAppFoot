# Generated by Django 2.2.4 on 2019-08-06 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placedispo', models.IntegerField(default=0)),
                ('placelibre', models.IntegerField(default=0)),
                ('heure', models.IntegerField(default=0)),
                ('minute', models.IntegerField(default=0)),
                ('départ', models.CharField(max_length=255)),
                ('p1', models.IntegerField(blank=True, null=True)),
                ('addr1', models.CharField(blank=True, max_length=255, null=True)),
                ('p2', models.IntegerField(blank=True, null=True)),
                ('addr2', models.CharField(blank=True, max_length=255, null=True)),
                ('p3', models.IntegerField(blank=True, null=True)),
                ('addr3', models.CharField(blank=True, max_length=255, null=True)),
                ('p4', models.IntegerField(blank=True, null=True)),
                ('addr4', models.CharField(blank=True, max_length=255, null=True)),
                ('p5', models.IntegerField(blank=True, null=True)),
                ('addr5', models.CharField(blank=True, max_length=255, null=True)),
                ('p6', models.IntegerField(blank=True, null=True)),
                ('addr6', models.CharField(blank=True, max_length=255, null=True)),
                ('p7', models.IntegerField(blank=True, null=True)),
                ('addr7', models.CharField(blank=True, max_length=255, null=True)),
                ('conduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]