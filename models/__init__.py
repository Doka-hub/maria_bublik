from .models import objects, TGUser, migrator, migrate, DoesNotExist


def setup():
    if not TGUser.table_exists():
        TGUser.create_table()
