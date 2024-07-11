# clear_database.py

from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Clears the database schema and recreates the public schema.'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("DROP SCHEMA public CASCADE; CREATE SCHEMA public;")
            self.stdout.write(self.style.SUCCESS('Successfully cleared and recreated the database schema.'))
