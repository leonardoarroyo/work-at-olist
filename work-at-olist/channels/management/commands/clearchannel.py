from channels.models import Channel, Category
from channels.management.base import BaseChannelCommandMixin
from django.core.management.base import BaseCommand

from channels.management.helpers import get_input

class Command(BaseChannelCommandMixin, BaseCommand):
    help = "Remove all categories from a channel"

    def handle(self, *args, **options):
        channel_name = options['channel_name']
        self.verbosity = options['verbosity']

        # Running with verbosity 0 also requires no-input
        if options['verbosity'] == 0 and not options['no_input']:
            self._print("[ERR] Running with verbosity=0 requires flag --no-input.", 0, file=self.stderr)
            exit(1)

        # Confirm channel clearing
        if not options['no_input']:
            user_input = get_input("This will remove all categories for channel '{}'. Do you want to proceed? [y/N] ".format(channel_name))

            if user_input.lower().strip() != "y":
                self._print("Not proceeding.", 1)
                exit(0)

        # Check for channel existence
        try:
            channel = Channel.objects.get(name=channel_name)
        except Channel.DoesNotExist:
            self._print("[ERR] Channel '{}' does not exist.".format(channel_name), 0, file=self.stderr)
            exit(1)

        # Delete categories
        categories = Category.objects.filter(channel=channel)
        self._print("Deleting {} categories.".format(categories.count()), 1)

        if options['verbosity'] == 2:
            for category in categories:
                self._print("-- Deleting category {}, named '{}'".format(category.id, category.name), 2)

        if not options['dry_run']:
            categories.delete()
