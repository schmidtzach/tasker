# Generated by Django 4.2.7 on 2023-11-27 18:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="description",
            field=models.TextField(null=True),
        ),
    ]
