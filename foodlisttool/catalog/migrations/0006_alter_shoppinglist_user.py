# Generated by Django 5.1.3 on 2024-12-13 08:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_ingredient_image_userinfo_recipe_creator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.userinfo'),
        ),
    ]
