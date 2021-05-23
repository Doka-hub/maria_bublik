from pathlib import Path

from decouple import config


# PATH settings
BASE_DIR = Path(__file__).parent.parent
LOGS_BASE_PATH = str(BASE_DIR / 'logs')

# BOT settings
BOT_PLACE = config('BOT_PLACE', 'locale')
BOT_TOKEN = config('BOT_TOKEN')
BASE_URL = config('BASE_URL')  # webhook domain
ADMINS = [
    539655707,  # Дока
    362044897  # Мария
]

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
    'host': config('POSTGRESQL_HOST', 'localhost'),
    'user': config('POSTGRESQL_USER', 'postgres'),
    'db': config('POSTGRESQL_DATABASE_NAME', 'maria_bublyk'),
}

MYSQL = {
    'host':     config('MYSQL_HOST', 'localhost'),
    'user':     config('MYSQL_USER', 'root'),
    'password': config('MYSQL_PASSWORD', None),
    'db':       config('MYSQL_DATABASE_NAME', None),
    'maxsize':  5,
    'port':     3306,
}

REDIS = {
    'host':     config('REDIS_URL', 'redis://127.0.0.1'),
    'port': config('REDIS_PORT', 6379)
}
