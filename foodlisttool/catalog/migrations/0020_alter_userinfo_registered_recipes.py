# Generated by Django 5.1.4 on 2024-12-16 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_userinfo_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='registered_recipes',
            field=models.ManyToManyField(null=True, to='catalog.recipe'),
        ),
    ]
