"""App configuration for the Sticky Notes application."""

from django.apps import AppConfig


class StickynotesConfig(AppConfig):
    """Configuration class for the Sticky Notes app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "stickynotes"
