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

