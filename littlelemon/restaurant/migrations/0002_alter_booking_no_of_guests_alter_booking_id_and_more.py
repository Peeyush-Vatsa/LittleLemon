# Generated by Django 4.2.5 on 2023-10-09 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='No_of_guests',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Inventory',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
