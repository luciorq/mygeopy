# My `geopy` Library

Project developed during the URSSI 2025 Summer School.

Using `pytest` and `doctest` for testing.

Using `mkdocs-material` for documentation.

Also, I need to check `myst-parser`.

## Testing

```bash
pixi init;

pixi add python pip;
# pixi run python -m pip install -e ".[examples,docs,tests]";
# `pytest` and `doctest` are in the `tests` `dependency-group`.
# `rich` and `click` are in the `cli` `optional-dependencies`.
pixi run python -m pip install --group=all --editable .[cli];

pixi run python -m pytest -vvv;
```

## Build Documentation

```bash
pixi run python -m mkdocs new .;

pixi run python -m mkdocs build;
pixi run python -m mkdocs serve;
```

## Building the Package

Check `pixi-build` Python backend.

```bash
# pixi run hatch build;
# on conda-forge the build module is available through `python-build` package.
pixi add python-build;
pixi run python -m build;
```

## Using `uv` as the environment manager

Using `uv` as the environment manager is closer to traditional development
workflows.

### Build package

```bash
# uv init;
# uv pip install --all-extras --editable .;
# uv pip install --group=tests --group=docs --editable .[cli];
# uv pip install --group=all --editable .[cli];

uv pip install --editable .[cli];

uv run --group=docs mkdocs serve;
uv tool run ruff check;
uv tool run rumdl check;
uv run --group tests pytest;
uv build;
```

### Should I use `uv publish`?

Check more on that.
