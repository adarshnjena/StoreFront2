# Generated by Django 4.0.4 on 2022-05-19 18:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('store', '0009_alter_cartitem_cart'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart', 'product')},
        ),
    ]
