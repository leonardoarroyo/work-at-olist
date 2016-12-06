from channels.management.helpers import get_input

class BaseChannelCommandMixin():
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
        if (self.options['verbosity'] >= verbosity_required) or file==self.stderr:
            print(text, file=file)

    def _check_verbosity(self):
        # Running with verbosity 0 also requires no-input
        if self.options['verbosity'] == 0 and not self.options['no_input']:
            self._print("[ERR] Running with verbosity=0 requires flag --no-input.", 0, file=self.stderr)
            exit(1)

    def _confirm_operation(self, text):
        if not self.options['no_input']:
            user_input = get_input("{} [y/N] ".format(text))

            if user_input.lower().strip() != "y":
                self._print("Not proceeding.", 1)
                exit(0)
