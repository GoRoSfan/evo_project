from django.contrib import admin

from .models import TempFile


@admin.register(TempFile)
class TempFileAdmin(admin.ModelAdmin):
    fields = ('file', 'life_time')
