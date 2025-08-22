# My `geopy` Library

Project developed during the URSSI 2025 Summer School.

Using `pytest` and `doctest` for testing.

Using `mkdocs-material` for documentation.
Also, I need to check `myst-parser`.

## Testing

```bash
pixi init;

pixi add python pip;
# `pytest` and `doctest` are in the `tests` `optional-dependencies`
pixi run python -m pip install -e ".[examples,docs,tests]";

pixi run python -m pytest -vvv;
```

## Build Documentation

```bash
pixi run python -m mkdocs new . ;

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

## Using `uv`

### Build package

```bash
# uv init
# uv pip install --all-extras --editable .
uv pip install --editable .[docs,tests]
uv tool run pytest
uv build
```

### Should I use `uv publish`?

Check more on that.
