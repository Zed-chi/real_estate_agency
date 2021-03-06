# Generated by Django 2.2.4 on 2020-10-20 09:39
from django.db import models
from django.db import migrations


def fill_flat_owner_field(apps, schema):
    owner_model = apps.get_model("property", "Owner")
    for owner in owner_model.objects.all():
        for flat in owner.flats.all():
            flat.owner.add(owner)


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0011_auto_20201020_0842"),
    ]

    operations = [
        migrations.RenameField("Flat", "owner", "owner_deprecated"),
        migrations.AddField("Flat", "owner", models.ManyToManyField("Owner")),
        migrations.RunPython(fill_flat_owner_field),
        migrations.RemoveField("Flat", "owner_deprecated"),
    ]
