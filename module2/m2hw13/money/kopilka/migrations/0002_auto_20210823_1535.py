# Generated by Django 3.2.6 on 2021-08-23 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kopilka', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='money',
            name='summ',
        ),
        migrations.AddField(
            model_name='money',
            name='category',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='money',
            name='pub_date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
