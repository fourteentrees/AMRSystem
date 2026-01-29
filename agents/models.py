from django.db import models

import secrets

# Actually legit
def keygenerator():
    return secrets.token_urlsafe(32)

class Agent(models.Model):
    name = models.CharField(max_length=100, help_text="This is for your reference")
    api_key = models.CharField(default=keygenerator, unique=True)
    rate_limit = models.IntegerField(default=1600, help_text="Ensure your agent implementation does not go over this number of requests in 2 hours.")  # requests per 2 hours

    # Will return song requests sent in after this date.
    last_polled_songrequests = models.DateTimeField(auto_now=True)
    last_ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"