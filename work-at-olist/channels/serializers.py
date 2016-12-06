from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from channels import models

class RecursiveCategorySerializer(serializers.ModelSerializer):
    """ Used to retrieve categories recursively """
    categories = RecursiveField("RecursiveCategorySerializer", source="direct_children_category_set", many=True)

    class Meta:
        model = models.Category
        fields = ["uuid", "name", "categories"]
        ordering = ("uuid",)


class ChannelListSerializer(serializers.ModelSerializer):
    """ Used to retrieve a list of channels """

    class Meta:
        model = models.Channel
        fields = ["uuid", "name"]


class ChannelRetrieveSerializer(serializers.ModelSerializer):
    """ Used to retrieve a single channel """
    categories = RecursiveCategorySerializer(source="direct_children_category_set", many=True)

    class Meta:
        model = models.Channel
        fields = ["uuid", "name", "categories"]

