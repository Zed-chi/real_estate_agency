from django.contrib import admin

from .models import Flat


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


admin.site.register(Flat, FlatAdmin)
