from django.db import models

class AdCrawl(models.Model):
    friendly_name = models.CharField(max_length=255)
    content = models.TextField()
    campaign = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    can_run_on_stars = models.BooleanField(default=False, verbose_name="Can run on STARs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    run_through = models.DateTimeField(auto_now=False, null=True, blank=True, help_text="Leave blank to run forever.")
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.friendly_name} ({self.campaign})"
    
    class Meta:
        verbose_name = "Ad Crawl"
        verbose_name_plural = "Ad Crawls"

class AdCrawlRequests(models.Model):
    friendly_name = models.CharField(max_length=255)
    content = models.TextField()
    campaign = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    requested_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, help_text="Set this to yourself. WE KNOW WHO YOU ARE.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request for {self.friendly_name} by {self.requested_by}"
    
    class Meta:
        verbose_name = "Ad Crawl Request"
        verbose_name_plural = "Ad Crawl Requests"