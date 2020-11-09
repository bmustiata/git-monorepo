#!/usr/bin/env python
import sys

import click


@click.command()
@click.argument("edited_file")
def main(edited_file: str) -> None:
    """
    This code does nothing on purpose. This is to be used as a git
    editor, and automatically commit the files.
    """
    with open(edited_file, "rt", encoding="utf-8") as f:
        print(f.read())

    sys.exit(1)


if __name__ == '__main__':
    main()
