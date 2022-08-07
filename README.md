# What about the size
Utility to recursively explore file sizes in directory

---
### Installation
```commandline
pip3 install --upgrade git+https://github.com/mnogom/what-about-the-size.git
```

---
### Usage
```commandline
  -h, --help            show this help message and exit
  -p PATH, --path PATH
  -s STYLE, --style STYLE
  -i [IGNORE_DIRS ...], --ignore-dirs [IGNORE_DIRS ...]
```

---
### Features
1. To output styles: ***tree*** and ***plain (with order by weight)***
2. Ignore directories

*See examples below*

### To do:
1. Add minimal limitation for weight
2. Ignore regex patterns

---
### Examples
#### tree output
```shell
# poetry run wats -i .venv .git .idea
├─ .
│  ├─ wats
│  │  ├─ __pycache__
│  │  │  • __init__.cpython-39.pyc :: [ 0.17 kB ]
│  │  │  • builder.cpython-39.pyc :: [ 2.07 kB ]
│  │  │  • cli.cpython-39.pyc :: [ 0.82 kB ]
│  │  │  • files.cpython-39.pyc :: [ 1.29 kB ]
│  │  ├─ renders
│  │  │  ├─ __pycache__
│  │  │  │  • __init__.cpython-39.pyc :: [ 0.44 kB ]
│  │  │  │  • plain.cpython-39.pyc :: [ 1.88 kB ]
│  │  │  │  • tree_render.cpython-39.pyc :: [ 1.96 kB ]
│  │  │  │  • utils.cpython-39.pyc :: [ 0.52 kB ]
│  │  │  • __init__.py :: [ 0.22 kB ]
│  │  │  • plain.py :: [ 1.1 kB ]
│  │  │  • tree_render.py :: [ 1.6 kB ]
│  │  │  • utils.py :: [ 0.17 kB ]
│  │  ├─ script
│  │  │  ├─ __pycache__
│  │  │  │  • __init__.cpython-39.pyc :: [ 0.17 kB ]
│  │  │  │  • wats.cpython-39.pyc :: [ 0.57 kB ]
│  │  │  • __init__.py :: [ 0.0 kB ]
│  │  │  • wats.py :: [ 0.35 kB ]
│  │  • __init__.py :: [ 0.0 kB ]
│  │  • builder.py :: [ 1.49 kB ]
│  │  • cli.py :: [ 0.66 kB ]
│  │  • files.py :: [ 0.54 kB ]
│  • .gitignore :: [ 0.1 kB ]
│  • Makefile :: [ 0.08 kB ]
│  • README.md :: [ 0.00 kB ]
│  • poetry.lock :: [ 1.55 kB ]
│  • pyproject.toml :: [ 0.52 kB ]
```
#### plain output
```shell
# poetry run wats -i .venv .git .idea -s plain
[ 2.07 kB ] :: /wats/__pycache__/builder.cpython-39.pyc
[ 1.96 kB ] :: /wats/renders/__pycache__/tree_render.cpython-39.pyc
[ 1.88 kB ] :: /wats/renders/__pycache__/plain.cpython-39.pyc
[ 1.6 kB ] :: /wats/renders/tree_render.py
[ 1.55 kB ] :: /poetry.lock
[ 1.49 kB ] :: /wats/builder.py
[ 1.29 kB ] :: /wats/__pycache__/files.cpython-39.pyc
[ 1.1 kB ] :: /wats/renders/plain.py
[ 0.82 kB ] :: /wats/__pycache__/cli.cpython-39.pyc
[ 0.66 kB ] :: /wats/cli.py
[ 0.57 kB ] :: /wats/script/__pycache__/wats.cpython-39.pyc
[ 0.54 kB ] :: /wats/files.py
[ 0.52 kB ] :: /wats/renders/__pycache__/utils.cpython-39.pyc
[ 0.52 kB ] :: /pyproject.toml
[ 0.44 kB ] :: /wats/renders/__pycache__/__init__.cpython-39.pyc
[ 0.35 kB ] :: /wats/script/wats.py
[ 0.22 kB ] :: /wats/renders/__init__.py
[ 0.17 kB ] :: /wats/script/__pycache__/__init__.cpython-39.pyc
[ 0.17 kB ] :: /wats/renders/utils.py
[ 0.17 kB ] :: /wats/__pycache__/__init__.cpython-39.pyc
[ 0.1 kB ] :: /.gitignore
[ 0.08 kB ] :: /Makefile
[ 0.00 kB ] :: /README.md
[ 0.0 kB ] :: /wats/script/__init__.py
[ 0.0 kB ] :: /wats/__init__.py
```
