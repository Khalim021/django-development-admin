
from django.contrib import admin

# Register your models here.
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['user', 'bio']
    list_filter = ['created', 'updated']


