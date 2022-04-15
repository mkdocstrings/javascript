"""This module implements a renderer for the Javascript language."""

from __future__ import annotations

from markdown import Markdown
from markupsafe import Markup
from mkdocstrings.extension import PluginError
from mkdocstrings.handlers.base import BaseRenderer, CollectorItem
from mkdocstrings.loggers import get_logger

logger = get_logger(__name__)


class JavascriptRenderer(BaseRenderer):
    """The class responsible for loading Jinja templates and rendering them.

    It defines some configuration options, implements the `render` method,
    and overrides the `update_env` method of the [`BaseRenderer` class][mkdocstrings.handlers.base.BaseRenderer].

    Attributes:
        fallback_theme: The theme to fallback to.
        default_config: The default rendering options.
    """

    fallback_theme = "material"

    default_config: dict = {
        "show_root_heading": False,
        "show_root_toc_entry": True,
        "heading_level": 2,
    }
    """The default rendering options.

    Option | Type | Description | Default
    ------ | ---- | ----------- | -------
    **`show_root_heading`** | `bool` | Show the heading of the object at the root of the documentation tree. | `False`
    **`show_root_toc_entry`** | `bool` | If the root heading is not shown, at least add a ToC entry for it. | `True`
    **`show_source`** | `bool` | Show the source code of this object. | `True`
    **`heading_level`** | `int` | The initial heading level to use. | `2`
    """  # noqa: E501

    def render(self, data: CollectorItem, config: dict) -> str:  # noqa: D102 (ignore missing docstring)
        raise PluginError("Implement me!")

        # final_config = {**self.default_config, **config}
        # heading_level = final_config["heading_level"]
        # template = self.env.get_template(f"{data...}.html")
        # return template.render(
        #     **{"config": final_config, data...: data, "heading_level": heading_level, "root": True},
        # )

    def update_env(self, md: Markdown, config: dict) -> None:  # noqa: D102 (ignore missing docstring)
        super().update_env(md, config)
        self.env.trim_blocks = True
        self.env.lstrip_blocks = True
        self.env.keep_trailing_newline = False
        self.env.filters["crossref"] = self.do_crossref

    def do_crossref(self, path: str, brief: bool = True) -> Markup:
        """Filter to create cross-references.

        Parameters:
            path: The path to link to.
            brief: Show only the last part of the path, add full path as hover.

        Returns:
            Markup text.
        """
        full_path = path
        if brief:
            path = full_path.split(".")[-1]
        return Markup("<span data-autorefs-optional-hover={full_path}>{path}</span>").format(
            full_path=full_path, path=path
        )
