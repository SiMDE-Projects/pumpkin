# Generated by Django 4.1.7 on 2023-03-13 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pumpkin', '0011_alter_item_commentaire_alter_item_date_achat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_achat',
            field=models.DateField(default=None, null=True),
        ),
    ]
