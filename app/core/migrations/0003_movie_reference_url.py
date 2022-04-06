# Generated by Django 4.0.3 on 2022-04-06 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_label_movie"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="reference_url",
            field=models.URLField(default="https://google.com", max_length=250),
            preserve_default=False,
        ),
    ]
