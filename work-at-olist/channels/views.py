from django.shortcuts import render

from rest_framework import mixins
from rest_framework import viewsets

from channels import models
from channels import serializers

class ChannelResourceViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = models.Channel.objects.all()
    serializer_class = serializers.ChannelListSerializer
