# Generated by Django 5.1.3 on 2024-12-13 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_remove_recipe_creator'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]