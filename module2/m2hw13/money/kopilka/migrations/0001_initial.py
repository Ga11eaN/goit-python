# Generated by Django 3.2.6 on 2021-08-23 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('note_text', models.CharField(max_length=200)),
                ('earnings', models.FloatField(default=0)),
                ('summ', models.FloatField(default=0)),
            ],
        ),
    ]