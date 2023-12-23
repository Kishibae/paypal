# Generated by Django 2.2.4 on 2023-12-18 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bid', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]