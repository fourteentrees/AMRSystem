from django.contrib import admin
from .models import AdCrawl, AdCrawlRequests

admin.site.register(AdCrawl)
admin.site.register(AdCrawlRequests)