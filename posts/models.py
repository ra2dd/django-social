from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    content = models.CharField(max_length=512)

    created = models.DateTimeField(auto_now_add=True)

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
    )

    class Meta:
        ordering = ['-created']
        get_latest_by = ['-created']
