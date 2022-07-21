# Generated by Django 4.0.5 on 2022-07-21 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_commands_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commands',
            name='field',
            field=models.CharField(choices=[('Everyone', 'Everyone'), ('DJ', 'DJ'), ('Premium', 'Premium'), ('Admin', 'Admin')], default='Everyone', max_length=50),
        ),
    ]
