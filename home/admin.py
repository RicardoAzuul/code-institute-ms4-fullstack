from django.contrib import admin
from .models import Feature


class FeatureAdmin(admin.ModelAdmin):
    list_display = (
        'header',
        'text',
    )

    ordering = ('header',)

admin.site.register(Feature, FeatureAdmin)
