"""This module implements a handler for the Python language."""

from __future__ import annotations

from typing import Any

from mkdocstrings.handlers.base import BaseHandler

from mkdocstrings_handlers.javascript.collector import JavascriptCollector
from mkdocstrings_handlers.javascript.renderer import JavascriptRenderer


class JavascriptHandler(BaseHandler):
    """The Javascript handler class.

    Attributes:
        domain: The cross-documentation domain/language for this handler.
        enable_inventory: Whether this handler is interested in enabling the creation
            of the `objects.inv` Sphinx inventory file.
    """

    domain: str = "javascript"  # to match Sphinx's default domain
    enable_inventory: bool = False


def get_handler(
    theme: str,  # noqa: W0613 (unused argument config)
    custom_templates: str | None = None,
    **config: Any,
) -> JavascriptHandler:
    """Simply return an instance of `JavascriptHandler`.

    Arguments:
        theme: The theme to use when rendering contents.
        custom_templates: Directory containing custom templates.
        **config: Configuration passed to the handler.

    Returns:
        An instance of the handler.
    """
    return JavascriptHandler(
        collector=JavascriptCollector(),
        renderer=JavascriptRenderer("javascript", theme, custom_templates),
    )
