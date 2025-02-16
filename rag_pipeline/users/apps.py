import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "rag_pipeline.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import rag_pipeline.users.signals  # noqa: F401
