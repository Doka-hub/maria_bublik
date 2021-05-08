from .models import objects, MaterialFormat, TGUser, MessageTemplate, migrator, migrate, DoesNotExist


def setup():
    MaterialFormat.setup()
    TGUser.setup()
    MessageTemplate.setup()
