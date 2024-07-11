# clear_database.py

from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = 'Clears the SQLite database by deleting all tables.'

    def handle(self, *args, **options):
        try:
            with connection.cursor() as cursor:
                cursor.execute("PRAGMA foreign_keys = OFF;")
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
                tables = cursor.fetchall()
                for table in tables:
                    cursor.execute(f"DROP TABLE IF EXISTS {table[0]};")
            self.stdout.write(self.style.SUCCESS('Successfully cleared SQLite database tables.'))
        except OperationalError as e:
            raise CommandError(f'Failed to clear SQLite database tables: {e}')


