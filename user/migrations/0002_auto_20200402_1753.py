# Generated by Django 3.0.4 on 2020-04-02 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.TextField(blank=True, max_length=15),
        ),
    ]