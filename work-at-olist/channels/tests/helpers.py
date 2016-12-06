from django.test import TestCase
from django.core.management import call_command

import random
import string
import uuid

from channels import models

def random_string(length=12):
    """ Generates random string. Default length is 12 """

    return "".join(random.choice(string.ascii_lowercase) for i in range(length))

def create_sample_channels(amount=5):
    """ Create sample channels for testing. Defaults to 5 channels. """

    for i in range(amount):
        channel = models.Channel(name=random_string())
        channel.save()

def create_sample_categories(channel, amount=5):
    """ Create sample categories for testing. Defaults to 5 categories. """

    for i in range(amount):
        category = models.Category(name=random_string(), channel=channel)
        category.save()

def is_valid_uuid(uuid_to_test, version=4):
    """ Check if a given string is a valid uuid """
    try:
        uuid_obj = uuid.UUID(uuid_to_test, version=version)
    except ValueError: # pragma: no cover
        return False

    return str(uuid_obj) == uuid_to_test


class BaseChannelCommandTestCaseMixin(TestCase):
    """ Tests for any command which include BaseChannelCommandMixin """

    def test_no_verbosity_requires_no_input(self):
        """ Test calling clearchannel command with verbosity 0 requires --no-input """
        with self.assertRaises(SystemExit):
            call_command('clearchannel', 'abc', '-v 0', stdout=self.stdout, stderr=self.stderr)

        self.stderr.seek(0)
        self.assertTrue(self.stderr.read().strip() == "[ERR] Running with verbosity=0 requires flag --no-input.")
