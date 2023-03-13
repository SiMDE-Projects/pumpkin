# Generated by Django 4.1.7 on 2023-03-12 19:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pumpkin', '0008_alter_item_date_achat'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='creation_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='item',
            name='quantite',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='updated_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
