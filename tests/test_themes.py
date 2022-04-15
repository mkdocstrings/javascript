"""Tests for the different themes we claim to support."""

import pytest


@pytest.mark.parametrize(
    "plugin",
    [
        {"theme": "mkdocs"},
        {"theme": "readthedocs"},
        {"theme": {"name": "material"}},
    ],
    indirect=["plugin"],
)
@pytest.mark.parametrize(
    "identifier",
    [
        # TODO: add identifiers to this list!
    ],
)
def test_render_themes_templates_python(identifier, plugin):
    """Test rendering of a given theme's templates.

    Parameters:
        identifier: Parametrized identifier.
        plugin: Pytest fixture: [tests.conftest.fixture_plugin][].
    """
    handler = plugin.handlers.get_handler("javascript")
    handler.renderer._update_env(plugin.md, plugin.handlers._config)  # noqa: WPS437
    data = handler.collector.collect(identifier, {})
    handler.renderer.render(data, {})
