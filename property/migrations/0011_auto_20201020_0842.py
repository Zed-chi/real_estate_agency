# Generated by Django 2.2.4 on 2020-10-20 05:42

from django.db import migrations


def fill_owner_model_from_flat(apps, schema):
    flat_model = apps.get_model("property", "Flat")
    owner_model = apps.get_model("property", "Owner")
    for flat in flat_model.objects.all():
        owner = owner_model.objects.get_or_create(
                name=flat.owner,
                owners_phonenumber=flat.owners_phonenumber,
                owner_pure_phone=flat.owner_pure_phone,
            )
        owner.save()
        owner.flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0010_auto_20201020_0103"),
    ]

    operations = [migrations.RunPython(fill_owner_model_from_flat)]