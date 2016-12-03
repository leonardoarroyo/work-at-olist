import random
import string

from django.test import TestCase

from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from channels.tests import helpers


class ChannelResourceViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('channel-list')


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
