""" All apps running on the django project."""
from django.apps import AppConfig


class AtoolConfig(AppConfig):
    """ Configuration that is loaded for the project. """
    default_auto_field = 'django.db.models.BigAutoField'
    """ Set the primary key type for models wihtout primary key. """
    name = 'Antragsverwaltungstool'
    """ Name of the project. """
