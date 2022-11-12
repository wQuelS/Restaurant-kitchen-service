from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from restaurant.models import Dish, DishType, Cook, Ingredient


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "dish_type", "price"]
    list_filter = ["dish_type"]
    search_fields = ["name"]


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )


admin.site.register(DishType)
admin.site.register(Ingredient)
