# Generated by Django 5.1.3 on 2024-12-13 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_remove_shoppinglist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='creator',
        ),
    ]
