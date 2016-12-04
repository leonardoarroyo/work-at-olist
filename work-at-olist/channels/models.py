from django.db import models
import uuid

class Channel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300, unique=True)


class Category(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300)

    # Relationships
    channel = models.ForeignKey('channels.Channel')
    parent = models.ForeignKey('self', blank=True, null=True)
