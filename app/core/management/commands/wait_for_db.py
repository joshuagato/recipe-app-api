"""
Django command to wait for database to be available.
"""
from django.core.management.base import BaseCommand
# from django.db import connections


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        pass
        # """
        # Wait for database to be available.
        # """
        # while True:
        #     try:
        #         connections["default"].cursor().execute("SELECT 1")
        #         break
        #     except Exception:
        #         self.stdout.write("Waiting for database...")