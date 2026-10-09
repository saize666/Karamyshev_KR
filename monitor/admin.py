from django.contrib import admin
from .models import AccessEvent

@admin.register(AccessEvent)
class AccessEventAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'username', 'vm_name', 'device', 'decision', 'reason')
    list_filter = ('decision', 'device', 'vm_name')
    search_fields = ('username', 'vm_name', 'ip_address', 'reason')
    readonly_fields = ('created_at',)
