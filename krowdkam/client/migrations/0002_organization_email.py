# Generated by Django 3.2.3 on 2021-08-03 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='email',
            field=models.CharField(default='', max_length=500),
        ),
    ]