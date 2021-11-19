# Python library with Rust extension

Built using pyo3 and poetry.

Based on [this video](https://www.youtube.com/watch?v=yqLD22sIYMo).

# Build

> Only checked on Ubuntu 18.04 with one version of Rust!

```bash
poetry build
poetry run pure-python
poetry run rust-extension
```
