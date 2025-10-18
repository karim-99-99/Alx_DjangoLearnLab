from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
# Create your models here.
class Notification(models.Model):


    recipient = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='actions')
    verb = models.CharField(max_length=20)
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    target_object_id = models.PositiveIntegerField(null=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')   
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
