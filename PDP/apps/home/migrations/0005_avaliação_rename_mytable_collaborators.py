# Generated by Django 5.0.6 on 2024-05-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_mytable_ano_mytable_data_mytable_diruni_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliação',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processCode', models.CharField(default='TI-03-2024', max_length=10)),
                ('numAvaliador', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='MyTable',
            new_name='Collaborators',
        ),
    ]
