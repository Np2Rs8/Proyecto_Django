# Generated by Django 4.1.1 on 2022-09-15 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_review"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactprofile",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="contactProfile"),
        ),
    ]
