# Generated by Django 3.2.6 on 2021-08-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kopilka', '0002_auto_20210823_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='category',
            field=models.CharField(default='None', max_length=20),
        ),
        migrations.AlterField(
            model_name='money',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]