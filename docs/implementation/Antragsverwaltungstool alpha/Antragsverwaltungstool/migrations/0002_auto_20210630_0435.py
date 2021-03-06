# Generated by Django 3.2.4 on 2021-06-30 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Antragsverwaltungstool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumberCount',
            fields=[
                ('number', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('legislature', models.CharField(max_length=7)),
                ('session', models.IntegerField()),
                ('ongoing_number', models.IntegerField()),
            ],
            options={
                'ordering': ['ongoing_number'],
            },
        ),
        migrations.AlterField(
            model_name='advisorymember',
            name='number',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='conduct',
            name='number',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='finance',
            name='number',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='number',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='universall',
            name='number',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, unique=True),
        ),
    ]
