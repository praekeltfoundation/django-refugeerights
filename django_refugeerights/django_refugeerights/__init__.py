from __future__ import absolute_import

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import locationfinder as locationfinder_app  # flake8: noqa