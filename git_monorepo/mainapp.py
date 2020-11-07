#!/usr/bin/env python3
import os
import subprocess
import sys
from typing import Any, Dict
from termcolor_util import yellow

import click
import yaml


@click.group()
def main():
    pass


@click.command("help")
@click.argument("command")
def help(command) -> None:
    with click.Context(main) as ctx:
        if "pull" == command:
            click.echo(pull.get_help(ctx))
        elif "push" == command:
            click.echo(pull.get_help(ctx))
        else:
            click.echo(f"Unknown command {command}")
            sys.exit(1)


@click.command("pull")
def pull() -> None:
    with open("gerepo.yml", "rt") as f:
        config_data = yaml.safe_load(f)

    repos: Dict[str, str] = dict()
    merge_repos(
        path="",
        repos=repos,
        data=config_data["mappings"]
    )

    for folder_name, repo_location in repos.items():
        print(yellow(repo_location, bold=True),
              yellow("->"),
              yellow(folder_name, bold=True),
              )
        if not os.path.isdir(folder_name):
            subprocess.check_call([
                "git", "subtree", "add", "-P", folder_name, repo_location, "master"
            ])
            continue

        subprocess.check_call([
            "git", "subtree", "pull", "-P", folder_name, repo_location, "master"
        ])


@click.command("push")
def push() -> None:
    print("hello click a")


main.add_command(pull)
main.add_command(push)
main.add_command(help)


if __name__ == '__main__':
    main()


def merge_repos(*, repos: Dict[str, str], path: str, data: Dict[str, Any]) -> None:
    for key_name, key_value in data.items():
        relative_path = os.path.join(path, key_name)

        if isinstance(key_value, str):
            repos[relative_path] = key_value
            continue

        merge_repos(
            repos=repos,
            path=relative_path,
            data=key_value,
        )
