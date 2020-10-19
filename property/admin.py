from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ["town", "address", "owner"]
    readonly_fields = ["created_at"]
    list_display = ("address", "price", "new_building", "created_at", "town")
    list_editable = ["new_building"]
    list_filter = [
        "new_building",
        "owners_phonenumber",
        "created_at",
        "price",
        "town",
        "floor",
        "rooms_number",
        "living_area",
        "has_balcony",
        "construction_year",
    ]


class ComplaintAdmin(admin.ModelAdmin):
    search_fields = ["complaining_user", "complained_on_flat"]
    raw_id_fields = ("complaining_user", "complained_on_flat")


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)

