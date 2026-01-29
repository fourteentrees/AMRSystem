from django.contrib import admin
from django.core.exceptions import PermissionDenied
from .models import AdCrawl, AdCrawlUserPerms

class AdCrawlAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'campaign', 'creator', 'get_status_display', 'can_run_on_stars', 'created_at', 'updated_at')   
    
    def get_status_display(self, obj):
        """Display status as readable text"""
        status_choices = {
            0: 'Awaiting Moderation',
            1: 'Approved',
            2: 'Denied'
        }
        return status_choices.get(obj.status, 'Unknown')
    
    get_status_display.short_description = 'Status'

    def get_readonly_fields(self, request, obj=None):
        """Make status and reason_for_denial read-only for non-moderators"""
        readonly = list(super().get_readonly_fields(request, obj))
        
        # Creator is always read-only
        readonly.append('creator')
        
        # Check if user has moderation permission
        has_mod_perm = (
            request.user.is_superuser or
            AdCrawlUserPerms.objects.filter(
                user=request.user, 
                can_moderate=True
            ).exists()
        )
        
        # If user can't moderate, make status/reason_for_denial read-only
        if not has_mod_perm:
            readonly.extend(['status', 'reason_for_denial'])
        
        return readonly
    
    def get_queryset(self, request):
        """Filter queryset based on permissions"""
        qs = super().get_queryset(request)
        
        # Superusers see everything
        if request.user.is_superuser:
            return qs
        
        # Check if user can edit others' crawls
        can_edit_others = AdCrawlUserPerms.objects.filter(
            user=request.user,
            can_edit_others_crawls=True
        ).exists()
        
        # If they can't edit others, only show their own
        if not can_edit_others:
            return qs.filter(creator=request.user)
        
        return qs
    
    def save_model(self, request, obj, form, change):
        """Set creator to current user on creation"""
        if not change:  # If creating new object
            obj.creator = request.user
        super().save_model(request, obj, form, change)

admin.site.register(AdCrawl, AdCrawlAdmin)
admin.site.register(AdCrawlUserPerms)