from django.db import models

class AdCrawl(models.Model):
    friendly_name = models.CharField(max_length=255)
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    campaign = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    can_run_on_stars = models.BooleanField(default=False, verbose_name="Can run on STARs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    run_through = models.DateTimeField(auto_now=False, null=True, blank=True, help_text="Leave blank to run forever.")
    status = models.IntegerField(default=0, help_text="0 = awaiting moderation, 1 = approved, 2 = denied")
    reason_for_denial = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.friendly_name} ({self.campaign})"
    
    class Meta:
        verbose_name = "Ad Crawl"
        verbose_name_plural = "Ad Crawls"

class AdCrawlUserPerms(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    can_moderate = models.BooleanField(default=False)
    can_edit_others_crawls = models.BooleanField(default=False)

    def __str__(self):
        return f"Permissions for {self.user.username}"
    
    class Meta:
        verbose_name = "Ad Crawl User Permission"
        verbose_name_plural = "Ad Crawl User Permissions"