from channels.models import Channel, Category
from channels.management.base import BaseChannelCommandMixin
from django.core.management.base import BaseCommand

class Command(BaseChannelCommandMixin, BaseCommand):
    help = "Remove all categories from a channel"

    def handle(self, *args, **options):
        channel_name = options['channel_name']
        self.options = options

        self._check_verbosity()

        # Confirm channel clearing
        self._confirm_operation("This will remove all categories for channel '{}'. Do you want to proceed?".format(channel_name))

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
