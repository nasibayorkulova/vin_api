from django.contrib import admin
from .models import VIN


# Register a model to manage them on the admin panel.
class VinAdmin(admin.ModelAdmin):
    list_display = ('vin', 'year', 'make', 'model', 'type', 'color', 'dimensions', 'weight')
    list_filter = ('year', 'make', 'type')
    search_fields = ('vin',)


admin.site.register(VIN, VinAdmin)
