# Generated by Django 3.2 on 2023-01-31 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_productcomment'),
        ('wishlist', '0002_auto_20230130_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='products',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='products',
            field=models.ManyToManyField(related_name='product_wishlists', through='wishlist.wishlistItem', to='products.Product'),
        ),
    ]
