# Generated by Django 4.1.7 on 2023-03-13 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pumpkin', '0013_alter_item_etat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_achat',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
