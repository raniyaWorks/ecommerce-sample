# Generated by Django 2.2 on 2021-06-26 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['date_added']},
        ),
        migrations.AlterModelTable(
            name='cart',
            table='cart',
        ),
        migrations.AlterModelTable(
            name='cartitem',
            table='cartitem',
        ),
    ]