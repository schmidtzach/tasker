# Generated by Django 4.2.7 on 2023-11-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_project_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.TextField(default="This task need's to be complete"),
        ),
    ]