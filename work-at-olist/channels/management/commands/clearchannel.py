from channels.models import Channel, Category
from django.core.management.base import BaseCommand

from channels.management.helpers import get_input

class Command(BaseCommand):
    help = "Remove all categories from a channel"

    def add_arguments(self, parser):
        # Channel name used to find channel
        parser.add_argument('channel_name', type=str)

        # Run the command without user input. Used for automation.
        parser.add_argument(
            "--no-input",
            action="store_true",
            dest="no_input",
            default=False,
            help="Does not ask for any confirmation before executing actions"
        )

        # Test command without commiting changes
        parser.add_argument(
            "--dry-run",
            action="store_true",
            dest="dry_run",
            default=False,
            help="Test the command without commiting changes"
        )

    def _print(self, text, verbosity_required, file=None):
        """ Only output a text if verbosity set to equal or higher than text verbosity level """
        file = file or self.stdout
        if (self.verbosity >= verbosity_required) or file==self.stderr:
            print(text, file=file)


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
