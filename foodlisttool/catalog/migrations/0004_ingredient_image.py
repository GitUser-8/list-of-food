# Generated by Django 5.1.3 on 2024-12-12 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_shoppinglist_ing_list_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
