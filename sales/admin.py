from django.contrib import admin

# Register your models here.
from sales.models import Position, Sales, CSV


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    search_fields = ['product', 'quantity', 'price']
    list_filter = ['created']


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    search_fields = ['customer', 'sales_man']
    list_filter = ['created', 'updated']


@admin.register(CSV)
class CSVAdmin(admin.ModelAdmin):
    search_fields = ['file_name']
    list_filter = ['created', 'updated']





