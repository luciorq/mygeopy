# My `geopy` Library

Project developed during the URSSI 2025 Summer School.

Using `pytest` and `doctest` for testing.

## Testing

```bash
pixi init;

pixi add python pip;
# `pytest` and `doctest` are in the `tests` `optional-dependencies`
pixi run python -m pip install -e ".[tests]";

pixi run python -m pytest;
```
