from django.contrib import admin
from .models import BodyPart, Equipment, Target, Workout

# Register your models here.


class WorkoutAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "bodypart",
        "equipment",
        "target",
        "rating",
        "image",
    )

    ordering = ("name",)


class BodyPartAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )

    ordering = ("friendly_name",)


class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )

    ordering = ("friendly_name",)


class TargetAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )

    ordering = ("friendly_name",)


admin.site.register(BodyPart, BodyPartAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Target, TargetAdmin)
