# Generated by Django 4.1.7 on 2023-03-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pumpkin', '0010_alter_item_creation_date_alter_item_date_achat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='commentaire',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='date_achat',
            field=models.DateField(blank=True, default=None),
        ),
    ]
