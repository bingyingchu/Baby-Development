from django.contrib import admin
from .models import Users


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("week",)
    ordering = ("first_name",)
    readonly_fields = ("week",)


admin.site.register(Users, FormAdmin)

