<div align="center">

# riptree

<img src="https://raw.githubusercontent.com/Diplo2by/riptree/main/assets/logo.png" alt="riptree logo" width="250"/>

**A beautiful tree command that respects .gitignore with colorful file icons**

[![PyPI version](https://badge.fury.io/py/riptree.svg)](https://badge.fury.io/py/riptree)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

</div>

## Features

- Beautiful icons for different file types
- Special icons for common folder names
- Respects `.gitignore` automatically
- Fast and lightweight
- Clean tree structure visualization

## Installation

```bash
pip install riptree
```

## Requirements

- Python 3.7+
- Git repository

## Usage

```bash
# Show tree with icons (default)
riptree

# Show tree without icons
riptree --no-icons

# List all available icons
riptree --list-icons

# Show version
riptree --version
```

## Example Output

```bash
.
├── 📁 src
│   ├── 🐍 main.py
│   ├── 📜 utils.js
│   └── ⚛️ App.tsx
├── 🧪 tests
│   └── 🐍 test_main.py
├── 📝 README.md
├── 📦 package.json
└── 🙈 .gitignore

2 directories, 6 files
```

## Supported File Types

See all supported file types and their icons:

```bash
riptree --list-icons
```
