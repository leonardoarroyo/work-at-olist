from django.shortcuts import render

from rest_framework import mixins
from rest_framework import viewsets

from channels import models
from channels import serializers

class ChannelResourceViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = models.Channel.objects.all()
    lookup_field = "name"

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.ChannelListSerializer
        if self.action == "retrieve":
            return serializers.ChannelRetrieveSerializer

class CategoryResourceViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.Category.objects.all()
    lookup_field = "uuid"

    def get_serializer_class(self):
        if self.action == "retrieve":
            return serializers.CategoryRetrieveSerializer
