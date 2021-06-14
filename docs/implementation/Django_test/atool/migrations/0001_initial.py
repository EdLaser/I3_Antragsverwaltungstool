# Generated by Django 3.2.3 on 2021-06-02 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvisoryMember',
            fields=[
                ('flag', models.IntegerField(default=0)),
                ('number', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=25, null=True)),
                ('office', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=25, null=True)),
                ('mail', models.EmailField(max_length=30, null=True)),
                ('text', models.CharField(max_length=260, null=True)),
                ('frg1', models.CharField(max_length=260, null=True)),
                ('frg2', models.CharField(max_length=260, null=True)),
                ('frg3', models.CharField(max_length=260, null=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
    ]