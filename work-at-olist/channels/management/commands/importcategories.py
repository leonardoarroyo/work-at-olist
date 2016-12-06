from channels.models import Channel, Category
from channels.management.base import BaseChannelCommandMixin
from django.core.management.base import BaseCommand
from django.core.management import call_command

from channels.management.helpers import get_input

import csv


class Command(BaseChannelCommandMixin, BaseCommand):
    help = "Clear a channel and add category tree from csv file"

    def _read_category_csv(self, file):
        with open(file, 'r') as f:
            reader = csv.reader(f, delimiter=";")

            category_list = []
            column_index = None

            for row in reader:
              # reader is not subscriptable
              # we have to do some weird ifs if we don't want to cast
              # it to a list

              if column_index is not None:
                category_list.append(row[column_index])
              else:
                for i, column in enumerate(row):
                  if column.lower().strip() == "category":
                    column_index = i
                    break

                if column_index == None:
                  # If no column named 'category' is found on the header
                  self._print('Category column not found on csv.', 1, file=self.stderr)
                  exit(1)

            return category_list

    def _generate_category_tree_from_list(self, category_path_list):
        tree = {}

        for category_path in category_path_list:
            categories = category_path.split('/')

            pointer = tree
            for category_name in categories:
                pointer = pointer.setdefault(category_name.strip(), {})

        return tree


    def _generate_tree_from_csv(self, file):
        category_list = self._read_category_csv(file)
        return self._generate_category_tree_from_list(category_list)


    def _create_category_recursively(self, channel, d, parent=None):
        for k, v in d.items():
            category = Category(name=k, channel=channel)

            if parent:
              category.parent = parent

            self._print("Creating category '{}', parent '{}'".format(k, parent), 2, file=self.stdout)

            category.save()
            self._create_category_recursively(channel, v, parent=category)


    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)

        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        channel_name = options['channel_name']
        self.options = options

        self._check_verbosity()

        self._confirm_operation("Proceeding will wipe all categories in channel '{}' and overwrite them with categories from specified file. Do you want to proceed?".format(channel_name))

        category_tree = self._generate_tree_from_csv(options['csv_file'])

        channel = Channel.objects.get_or_create(name=channel_name)[0]

        self._print("Clearing channel.", 1, file=self.stdout)
        call_command('clearchannel', channel_name, '-v0', '--no-input')

        self._print("Creating category tree.", 1, file=self.stdout)
        self._create_category_recursively(channel, category_tree)
