# Generated by Django 3.2 on 2021-04-21 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20210421_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='custom_link',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
