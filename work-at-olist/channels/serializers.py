from rest_framework import serializers

from channels import models

class ChannelListSerializer(serializers.ModelSerializer):
    """ Used to retrieve a list of channels """

    class Meta:
        model = models.Channel
        fields = ['uuid', 'name']
