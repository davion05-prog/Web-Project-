from django.contrib import admin
from .models import Assignment


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "due_date", "status", "assigned_to")
    list_filter = ("status", "course")
    search_fields = ("title",)

# Register your models here.
