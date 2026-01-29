from django.contrib import admin
from .models import Agent

# Register your models here.
class AgentAdmin(admin.ModelAdmin):
    readonly_fields = ('api_key','last_ip_address','last_polled_songrequests',)
    list_display = ('name', 'last_ip_address', 'last_polled_songrequests',)


admin.site.register(Agent, AgentAdmin)