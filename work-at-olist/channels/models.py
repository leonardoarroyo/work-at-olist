from django.db import models
import uuid

class Channel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300)

    # Relationships
    channel = models.ForeignKey('channels.Channel')
    parent = models.ForeignKey('self', blank=True, null=True)


    class Meta:
        unique_together = ('name', 'parent', 'channel',)

    def __str__(self):
        return self.name
