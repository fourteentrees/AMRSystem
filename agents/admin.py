from django.contrib import admin
from .models import Agent

# Register your models here.
class AgentAdmin(admin.ModelAdmin):
    exclude = ('last_polled_songrequests',)

admin.site.register(Agent, AgentAdmin)