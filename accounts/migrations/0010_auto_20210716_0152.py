# Generated by Django 2.2.5 on 2021-07-15 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210715_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formbook',
            name='returning',
            field=models.IntegerField(default=0),
        ),
    ]