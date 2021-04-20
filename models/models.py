import peewee
from peewee import DoesNotExist
from peewee_async import Manager, PostgresqlDatabase, MySQLDatabase

from playhouse.migrate import MySQLMigrator, PostgresqlMigrator, migrate

from data import config


if config.BOT_PLACE == 'locale':
    database = MySQLDatabase(
        database=config.MYSQL['db'], user=config.MYSQL['user'], password=config.MYSQL['password']
    )
    migrator = MySQLMigrator(database)
else:
    database = PostgresqlDatabase(database=config.POSTGRESQL['db'], user=config.POSTGRESQL['user'])
    migrator = PostgresqlMigrator(database)


objects = Manager(database)


class BaseModel(peewee.Model):
    class Meta:
        database = database


class TGUser(BaseModel):
    LANGUAGE_CHOICES = (
        ('ru', 'ru'),
        ('en', 'en'),
    )

    user_id = peewee.IntegerField()
    username = peewee.CharField(max_length=255, null=True)
    phone_number = peewee.CharField(max_length=255, null=True)

    language = peewee.CharField(max_length=3, null=True, choices=LANGUAGE_CHOICES)

    blocked_by_user = peewee.BooleanField(default=False)
