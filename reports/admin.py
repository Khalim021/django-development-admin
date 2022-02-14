from django.contrib import admin

# Register your models here.
from reports.models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    search_fields = ['name', 'author']
    list_filter = ['created', 'updated']









