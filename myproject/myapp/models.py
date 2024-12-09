from django.db import models

# Create your models here.
class FortuneCookieTest(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()