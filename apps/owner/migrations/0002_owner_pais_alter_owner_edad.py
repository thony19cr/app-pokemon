# Generated by Django 4.1 on 2022-08-25 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='pais',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='owner',
            name='edad',
            field=models.CharField(max_length=3),
        ),
    ]
