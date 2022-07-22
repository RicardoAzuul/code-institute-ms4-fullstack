from django.contrib import admin
from .models import Feature


class FeatureAdmin(admin.ModelAdmin):
    """
    Makes the Feature model available in
    the admin portal for CRUD operations.
    """

    list_display = (
        "header",
        "text",
    )

    ordering = ("header",)


admin.site.register(Feature, FeatureAdmin)
