from django.core.management import BaseCommand


class Command(BaseCommand):
    """Command example https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/"""

    help = "Some help text"

    def handle(self, *args, **options):
        print("Passed")
