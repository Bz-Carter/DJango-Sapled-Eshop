# Generated by Django 4.1.7 on 2023-03-29 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0004_alter_review_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="product.product",
            ),
        ),
    ]