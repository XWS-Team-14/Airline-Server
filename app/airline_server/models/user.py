import uuid

from django.db import models


class User(models.Model):
    """Pseudo user created while waiting for upstream

    Attributes:
        id (UUID): Auto generated uuid used to uniquely indentify object
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

