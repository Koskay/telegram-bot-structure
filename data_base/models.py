import ormar

from .settings import base_ormar_config


class User(ormar.Model):

    ormar_config = base_ormar_config.copy(tablename="users")
