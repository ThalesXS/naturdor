# Generated by Django 5.0.6 on 2024-05-14 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=100)),
                ('field2', models.CharField(max_length=100)),
                ('field3', models.CharField(max_length=10)),
                ('field4', models.IntegerField()),
                ('field5', models.IntegerField()),
                ('field6', models.CharField(max_length=100)),
                ('field7', models.DateField()),
                ('field8', models.CharField(max_length=100)),
                ('field9', models.IntegerField()),
                ('field10', models.IntegerField()),
                ('field11', models.DateField()),
                ('field12', models.FloatField()),
                ('field13', models.FloatField()),
            ],
        ),
    ]
