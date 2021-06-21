# Generated by Django 3.2.3 on 2021-06-02 15:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('atool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('flag', models.IntegerField(default=0)),
                ('number', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=25, null=True)),
                ('office', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=25, null=True)),
                ('mail', models.EmailField(max_length=30, null=True)),
                ('text', models.CharField(max_length=260, null=True)),
                ('reason', models.CharField(max_length=260, null=True)),
                ('budget', models.CharField(max_length=260, null=True)),
                ('suggestion', models.CharField(max_length=260, null=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('flag', models.IntegerField(default=0)),
                ('number', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=25, null=True)),
                ('office', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=25, null=True)),
                ('mail', models.EmailField(max_length=30, null=True)),
                ('text', models.CharField(max_length=260, null=True)),
                ('frg1', models.CharField(max_length=260, null=True)),
                ('frg2', models.CharField(max_length=260, null=True)),
                ('frg3', models.CharField(max_length=260, null=True)),
                ('frg4', models.CharField(max_length=260, null=True)),
                ('frg_spez_1', models.CharField(max_length=260, null=True)),
                ('frg_spez_2', models.CharField(max_length=260, null=True)),
                ('frg_spez_3', models.CharField(max_length=260, null=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Universall',
            fields=[
                ('flag', models.IntegerField(default=0)),
                ('number', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=25, null=True)),
                ('office', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=25, null=True)),
                ('mail', models.EmailField(max_length=30, null=True)),
                ('text', models.CharField(max_length=260, null=True)),
                ('reason', models.CharField(max_length=260, null=True)),
                ('suggestion', models.CharField(max_length=260, null=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.AddField(
            model_name='advisorymember',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
