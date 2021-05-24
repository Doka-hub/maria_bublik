import peewee
from peewee import DoesNotExist
from peewee_async import Manager, PostgresqlDatabase, MySQLDatabase

from playhouse.migrate import MySQLMigrator, PostgresqlMigrator, migrate

from data import config

from .fields import JSONField


if config.BOT_PLACE == 'locale':
    database = MySQLDatabase(
        database=config.MYSQL['db'], user=config.MYSQL['user'], password=config.MYSQL['password']
    )
    migrator = MySQLMigrator(database)
else:
    database = PostgresqlDatabase(
        database=config.POSTGRESQL['db'], user=config.POSTGRESQL['user'], password=config.POSTGRESQL['password']
    )
    migrator = PostgresqlMigrator(database)


objects = Manager(database)


class BaseModel(peewee.Model):
    class Meta:
        database = database

    @classmethod
    def setup(cls):
        if not cls.table_exists():
            cls.create_table()


class MaterialFormat(BaseModel):
    name = peewee.CharField(max_length=255, unique=True, null=False)

    is_active = peewee.BooleanField(default=True)

    @classmethod
    def setup(cls):
        super().setup()
        for name in [
            'Вебiнары (безкоштовнi i платнi)',
            'Повний курс розмовноi англійськоi',
            'Drinking&Speaking club',
            'Я вже вчусь у вас'
        ]:
            cls.get_or_create(name=name)


class TGUser(BaseModel):
    LANGUAGE_CHOICES = (
        ('ru', 'ru'),
        ('en', 'en'),
    )

    user_id = peewee.IntegerField()
    username = peewee.CharField(max_length=255, null=True)
    phone_number = peewee.CharField(max_length=255, null=True)

    name = peewee.CharField(max_length=255, null=True)
    material_format = peewee.ForeignKeyField(MaterialFormat, backref='users', on_delete='SET NULL', null=True)

    language = peewee.CharField(max_length=3, null=True, choices=LANGUAGE_CHOICES)

    blocked_by_user = peewee.BooleanField(default=False)
    is_active = peewee.BooleanField(default=True)


class MessageTemplate(BaseModel):
    user = peewee.ForeignKeyField(TGUser, on_delete='CASCADE', related_name='message_templates')

    name = peewee.CharField(max_length=255, unique=True)
    data = JSONField()
