# Generated by Django 3.0.8 on 2020-10-19 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdms', '0005_auto_20201019_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficary',
            name='ben_contact',
            field=models.EmailField(default='mydefault@email.com', max_length=254),
        ),
    ]
