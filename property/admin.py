from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ["town", "address", "owner"]
    readonly_fields = ["created_at"]
    list_display = (
        "address",
        "price",
        "new_building",
        "created_at",
        "town",
        "owners_phonenumber",
        "owner_pure_phone",
    )
    list_editable = ["new_building"]
    list_filter = [
        "new_building",
        "price",
        "town",
        "rooms_number",
        "has_balcony",
        "construction_year",
    ]
    raw_id_fields = ("likes",)


class ComplaintAdmin(admin.ModelAdmin):
    search_fields = ["complaining_user", "complained_on_flat"]
    raw_id_fields = ("complaining_user", "complained_on_flat")


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flats",)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
