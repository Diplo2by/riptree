# riptree

A beautiful tree command that respects `.gitignore` with colorful file icons.

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
