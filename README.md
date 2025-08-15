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

```bash
pixi run hatch build;
```

## Should I use `uv publish`?

Check more on that.
