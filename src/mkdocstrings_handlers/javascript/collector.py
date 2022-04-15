"""This module implements a collector for the Javascript language."""

from __future__ import annotations

from mkdocstrings.handlers.base import BaseCollector, CollectionError, CollectorItem
from mkdocstrings.loggers import get_logger

logger = get_logger(__name__)


class JavascriptCollector(BaseCollector):
    """The class responsible for collecting data from source code."""

    default_config: dict = {}
    """The default selection options."""

    fallback_config: dict = {"fallback": True}

    def collect(self, identifier: str, config: dict) -> CollectorItem:  # noqa: WPS231
        """Collect the documentation tree given an identifier and selection options.

        Arguments:
            identifier: The identifier of an object.
            config: Selection options, used to alter the data collection.

        Raises:
            CollectionError: When there was a problem collecting the object documentation.
        """
        raise CollectionError("Implement me!")
