#!/usr/bin/env python3
"""
riptree - Run tree command while respecting .gitignore with file icons
"""

import subprocess
import sys
import os
import argparse
from pathlib import Path

from .icons import (
    FILE_ICONS,
    FOLDER_ICONS,
    DEFAULT_FILE_ICON,
    DEFAULT_FOLDER_ICON,
)

def get_icon(path, is_dir=False):
    """Get icon for a file or directory"""
    if is_dir:
        name = os.path.basename(path)
        return FOLDER_ICONS.get(name, DEFAULT_FOLDER_ICON)
    else:
        # Check exact filename matches first
        name = os.path.basename(path)
        if name in FILE_ICONS:
            return FILE_ICONS[name]

        # Then check extension
        ext = Path(path).suffix.lower()
        return FILE_ICONS.get(ext, DEFAULT_FILE_ICON)


def is_git_repo():
    """Check if current directory is a git repository"""
    try:
        subprocess.run(
            ["git", "rev-parse", "--git-dir"], capture_output=True, check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def get_git_files():
    """Get list of files tracked by git (respects .gitignore)"""
    try:
        result = subprocess.run(
            ["git", "ls-files"], capture_output=True, text=True, check=True
        )
        return result.stdout.strip().split("\n") if result.stdout.strip() else []
    except subprocess.CalledProcessError:
        return []


def build_tree_structure(files):
    """Build a tree structure from file list"""
    tree = {}

    for file in files:
        if not file:
            continue

        parts = Path(file).parts
        current = tree

        for i, part in enumerate(parts):
            if part not in current:
                is_last = i == len(parts) - 1
                current[part] = {} if not is_last else None
            current = current[part] if current[part] is not None else None
            if current is None:
                break

    return tree


def print_tree(tree, prefix="", is_last=True, show_icons=True):
    """Print tree structure with icons"""
    items = sorted(tree.items(), key=lambda x: (x[1] is None, x[0]))

    for i, (name, subtree) in enumerate(items):
        is_last_item = i == len(items) - 1

        # Determine if this is a directory
        is_dir = subtree is not None

        # Get icon
        icon = get_icon(name, is_dir) if show_icons else ""
        icon_str = f"{icon} " if icon else ""

        # Print current item
        connector = "└── " if is_last_item else "├── "
        print(f"{prefix}{connector}{icon_str}{name}")

        # Print subtree
        if is_dir and subtree:
            extension = "    " if is_last_item else "│   "
            print_tree(subtree, prefix + extension, is_last_item, show_icons)


def run_tree_with_icons(show_icons=True):
    """Run tree command with icons"""

    if not is_git_repo():
        print("Error: Not a git repository", file=sys.stderr)
        sys.exit(1)

    # Get git tracked files
    files = get_git_files()

    if not files:
        print("No git tracked files found", file=sys.stderr)
        sys.exit(1)

    # Build and print tree
    tree = build_tree_structure(files)
    print(".")
    print_tree(tree, show_icons=show_icons)

    # Print summary
    file_count = len(files)
    dir_count = len(set(str(Path(f).parent) for f in files if f))
    print(f"\n{dir_count} directories, {file_count} files")


def main():
    parser = argparse.ArgumentParser(
        description="riptree - Run tree command while respecting .gitignore with icons",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  riptree              Show tree with icons
  riptree --no-icons   Show tree without icons
        """,
    )

    parser.add_argument(
        "--no-icons", action="store_true", help="Disable file and folder icons"
    )

    parser.add_argument(
        "--list-icons", action="store_true", help="List all available icons and exit"
    )

    parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")

    args = parser.parse_args()

    if args.list_icons:
        print("File Icons:")
        for ext, icon in sorted(FILE_ICONS.items()):
            print(f"  {icon}  {ext}")
        print("\nFolder Icons:")
        for name, icon in sorted(FOLDER_ICONS.items()):
            print(f"  {icon}  {name}")
        sys.exit(0)

    run_tree_with_icons(show_icons=not args.no_icons)


if __name__ == "__main__":
    main()
