# Generated by Django 3.1.4 on 2021-05-26 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeInventory',
            fields=[
                ('_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('inv_name', models.CharField(max_length=200)),
            ],
        ),
    ]