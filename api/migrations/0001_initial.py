# Generated by Django 4.0.6 on 2022-07-20 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commands',
            fields=[
                ('name', models.CharField(max_length=46, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=100)),
                ('aliases', models.CharField(max_length=45)),
                ('is_premium', models.BooleanField(default=True)),
            ],
        ),
    ]
