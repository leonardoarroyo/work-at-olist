import os

from django.test import TestCase
from django.core.management import call_command
from unittest.mock import patch
from io import StringIO

from channels import models
from channels.tests import helpers



class ClearChannelCommandTestCase(helpers.BaseChannelCommandTestCaseMixin, TestCase):
    def setUp(self):
        self.stdout = StringIO()
        self.stderr = StringIO()

    @patch('channels.management.helpers.get_input', return_value="N")
    def test_ask_for_confirmation_without_no_input(self, input):
        """ Test calling clearchannel command without --no-input flag asks for user confirmation """
        with self.assertRaises(SystemExit):
            call_command('clearchannel', 'abc', stdout=self.stdout, stderr=self.stderr)

        self.stdout.seek(0)
        self.assertTrue(self.stdout.read().strip() == "Not proceeding.")

    def test_raises_error_inexistent_channel(self):
        """ Test calling clearchannel command for an inexistent channel returns an error """
        with self.assertRaises(SystemExit):
            call_command('clearchannel', 'abc', '--no-input', stdout=self.stdout, stderr=self.stderr)

        self.stderr.seek(0)
        self.assertTrue(self.stderr.read().strip() == "[ERR] Channel 'abc' does not exist.")

    def test_command_clears_channel(self):
        """ Test calling clearchannel command clears the channel """
        channel = models.Channel(name="testchannel")
        channel.save()
        helpers.create_sample_categories(channel, amount=10)

        self.assertTrue(channel.category_set.count() == 10)
        call_command('clearchannel', 'testchannel', '--no-input', stdout=self.stdout, stderr=self.stderr)
        self.stdout.seek(0)

        self.assertTrue(channel.category_set.count() == 0)
        self.assertTrue("Deleting 10 categories" in self.stdout.read().strip())


    def test_high_verbosity(self):
        """ Test calling clearchannel command  with high verbosity outputs category id and name """
        channel = models.Channel(name="testchannel")
        channel.save()
        helpers.create_sample_categories(channel, amount=10)
        test_strings = ["Deleting category {}, named '{}'".format(c.id, c.name) for c in models.Category.objects.filter(channel=channel)]

        self.assertTrue(channel.category_set.count() == 10)
        call_command('clearchannel', 'testchannel', '-v2', '--no-input', stdout=self.stdout, stderr=self.stderr)
        self.stdout.seek(0)
        out = self.stdout.read().strip()

        self.assertTrue(channel.category_set.count() == 0)
        self.assertTrue("Deleting 10 categories" in out)

        for test_string in test_strings:
          self.assertTrue(test_string in out)


class ImportCategoriesCommandTestCase(helpers.BaseChannelCommandTestCaseMixin, TestCase):
    def setUp(self):
        self.stdout = StringIO()
        self.stderr = StringIO()

    def test_no_category_column_error(self):
        """ Test calling importcategories command with no categories column raises error """
        file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/invalid_categories.csv'))

        with self.assertRaises(SystemExit):
            call_command('importcategories', 'abc', '--no-input', file, stdout=self.stdout, stderr=self.stderr),

        self.stderr.seek(0)
        self.stdout.seek(0)
        self.assertTrue(self.stderr.read().strip() == "Category column not found on csv.")


    def test_creates_category_tree(self):
        """ Test calling importcategories command with good csv creates category """
        file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/sample_categories.csv'))

        # Start creating dummy categories
        channel = models.Channel(name="testchannel")
        channel.save()
        helpers.create_sample_categories(channel, amount=10)

        # Assert dummy categories exist
        self.assertTrue(channel.category_set.count() == 10)

        call_command('importcategories', 'testchannel', file, '-v0', '--no-input', stdout=self.stdout, stderr=self.stderr),

        # Our sample csv has exactly 23 categories
        self.assertTrue(channel.category_set.count() == 23)
