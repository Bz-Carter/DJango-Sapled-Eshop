# Generated by Django 4.1.7 on 2023-03-29 10:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_review"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.IntegerField(default=0),
        ),
    ]
