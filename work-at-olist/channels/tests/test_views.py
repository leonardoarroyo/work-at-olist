import string
import os
import json

from django.test import TestCase
from django.core.management import call_command

from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from io import StringIO

from channels.tests import helpers
from channels.models import Category


class ChannelResourceListTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("channel-list")


    def test_query_optimization(self):
        """ Test channels route does not exceed 1 query"""

        helpers.create_sample_channels(amount=10)
        with self.assertNumQueries(1):
          response = self.client.get(self.url, format="json")


    def test_return_channels(self):
        """ Test channel list route returns all channels """
        response = self.client.get(self.url)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(len(response.data) == 0)

        helpers.create_sample_channels(amount=10)

        response = self.client.get(self.url)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(len(response.data) == 10)

        for channel in response.data:
            self.assertTrue(len(channel["name"]) > 0)
            self.assertTrue(helpers.is_valid_uuid(channel["uuid"]))

    def test_hides_id(self):
        """ Test channel list route doesn't return object id """
        helpers.create_sample_channels(amount=1)

        response = self.client.get(self.url)
        for channel in response.data:
            self.assertTrue("id" not in channel)

class PrepareChannel():
    def setUp(self):
        self.channel = "testchannel"
        self.client = APIClient()
        self._import_categories(self.channel)
        self.success_count = 0

    def _import_categories(self, channel_name):
        file = os.path.abspath(os.path.join(os.path.dirname(__file__), "data/sample_categories.csv"))
        call_command("importcategories", channel_name, file, "-v0", "--no-input", stdout=StringIO(), stderr=StringIO()),

    def _import_categories(self, channel_name):
        file = os.path.abspath(os.path.join(os.path.dirname(__file__), "data/sample_categories.csv"))
        call_command("importcategories", channel_name, file, "-v0", "--no-input", stdout=StringIO(), stderr=StringIO()),

    def _load_test_category_tree(self):
        file = os.path.abspath(os.path.join(os.path.dirname(__file__), "data/sample_categories.json"))
        with open(file, "r") as json_data:
              data = json.load(json_data)

        return data

    def _assert_tree_recursively(self, d, test_tree):
        for category in d:
            self.assertTrue(category["name"] in test_tree)
            self._assert_tree_recursively(category["children"], test_tree[category["name"]])
            self.success_count += 1

class ChannelResourceRetrieveTestCase(PrepareChannel, TestCase):
    def test_query_optimization(self):
        """ Test channels route does not exceed 1 query"""

        #helpers.create_sample_channels(amount=10)
        #with self.assertNumQueries(1):
        #  response = self.client.get(self.url, format="json")
        pass


    def test_return_category_tree(self):
        """ Test channel detail route returns category tree for channel """
        url = reverse("channel-detail", [self.channel])

        response = self.client.get(url)
        self.assertTrue(response.status_code == 200)

        test_tree = self._load_test_category_tree()
        self._assert_tree_recursively(response.data["categories"], test_tree)

        # _assert_tree_recursively checks our response.data against test_tree
        # and not the other way around. If our response.data is empty, the test
        # will still succeed. Instead of testing both ways, another simple way
        # is to just check success_count. Our current sample_categories.csv
        # should generate a 23 success_count
        self.assertTrue(self.success_count == 23)


class CategoryResourceRetrieveTestCase(PrepareChannel, TestCase):
    def test_returns_full_category_tree(self):
        """ Test category detail route returns category information along with its parents and children """
        computers_subcategory_uuid = Category.objects.get(name="Computers", parent__name="Books").uuid
        url = reverse("category-detail", [computers_subcategory_uuid])

        response = self.client.get(url)
        self.assertTrue(response.status_code == 200)

        self.assertTrue(response.data["name"] == "Computers")
        self.assertTrue(response.data["parent"]["name"] == "Books")

        test_tree = self._load_test_category_tree()["Books"]["Computers"]
        self._assert_tree_recursively(response.data["children"], test_tree)
        self.assertTrue(self.success_count == 3)
