from models import migrate, migrator

from playhouse.migrate import BooleanField


'''Здесь прописывать миграции'''
if __name__ == '__main__':
    migrate(
        migrator.add_column('TGUser', 'can_use_bot', BooleanField(default=True))
    )
