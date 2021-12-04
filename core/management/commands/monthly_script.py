# -*- coding: utf-8 -*-
import datetime
import logging

from django.core.management.base import BaseCommand

from core.utils import update_spaces

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Management command to update spaces
        """
        today = datetime.date.today()
        if today.day == 28:
            try:
                update_spaces()
            except Exception as e:
                logger.error(e)
