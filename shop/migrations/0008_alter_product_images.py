# Generated by Django 4.1.3 on 2023-06-09 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0007_remove_product_date_alter_contact_message_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="images",
            field=models.ImageField(default="", upload_to="shop/images/"),
        ),
    ]
