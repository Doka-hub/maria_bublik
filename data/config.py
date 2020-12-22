from pathlib import Path

from decouple import config


# PATH settings
BASE_DIR = Path(__file__).parent.parent
LOGS_BASE_PATH = str(BASE_DIR / 'logs')

# BOT settings
BOT_PLACE = config('BOT_PLACE')
BOT_TOKEN = config('BOT_TOKEN')
BASE_URL = config('BASE_URL')  # webhook domain
ADMINS = []

# WEBHOOK settings
WEBHOOK_PATH = f'/tg/webhooks/bot/{BOT_TOKEN}'
WEBHOOK_URL = f'{BASE_URL}{WEBHOOK_PATH}'

# I18N settings
I18N_DOMAIN = 'bot'
LOCALES_DIR = BASE_DIR / 'locales'

# TIMEZONE
TIMEZONE = config('TIMEZONE')

# DATABASE
POSTGRESQL = {
    'host': config('POSTGRESQL_HOST'),
    'user': config('POSTGRESQL_USER'),
    'db': config('POSTGRESQL_DATABASE_NAME'),
}
MYSQL = {
    'host':     config('MYSQL_HOST'),
    'user':     config('MYSQL_USER'),
    'password': config('MYSQL_PASSWORD'),
    'db':       config('MYSQL_DATABASE_NAME'),
    'maxsize':  5,
    'port':     3306,
}
REDIS = {
    'ip':     config('REDIS_URL', 'redis://127.0.0.1'),
    'port': config('REDIS_PORT', 6379)
}
