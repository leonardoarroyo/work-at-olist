from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from channels import models

class RecursiveDownwardCategorySerializer(serializers.ModelSerializer):
    """ Used to retrieve children categories recursively """
    children = RecursiveField("RecursiveDownwardCategorySerializer", source="direct_children_category_set", many=True)

    class Meta:
        model = models.Category
        fields = ["uuid", "name", "children"]

class RecursiveUpwardCategorySerializer(serializers.ModelSerializer):
    """ Used to retrieve parent categories recursively """
    parent = RecursiveField("RecursiveUpwardCategorySerializer")

    class Meta:
        model = models.Category
        fields = ["uuid", "name", "parent"]


class CategoryRetrieveSerializer(serializers.ModelSerializer):
    """ Retrieve a single category along with it's tree """
    children = RecursiveField("RecursiveDownwardCategorySerializer", source="direct_children_category_set", many=True)
    parent = RecursiveField("RecursiveUpwardCategorySerializer")

    class Meta:
        model = models.Category
        fields = ["uuid", "name", "children", "parent"]


class ChannelListSerializer(serializers.ModelSerializer):
    """ Used to retrieve a list of channels """

    class Meta:
        model = models.Channel
        fields = ["uuid", "name"]


class ChannelRetrieveSerializer(serializers.ModelSerializer):
    """ Used to retrieve a single channel """
    categories = RecursiveDownwardCategorySerializer(source="direct_children_category_set", many=True)

    class Meta:
        model = models.Channel
        fields = ["uuid", "name", "categories"]

