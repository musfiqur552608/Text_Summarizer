# Generated by Django 4.0.1 on 2022-01-08 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Summarizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mytext', models.CharField(max_length=1000000)),
                ('myword', models.IntegerField()),
                ('summarize', models.CharField(max_length=100000)),
                ('sumword', models.IntegerField()),
            ],
        ),
    ]