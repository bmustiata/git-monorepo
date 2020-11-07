#!/usr/bin/env python3
import os
from typing import List, Set, Any, Dict

import click
import sys
import adhesive
import yaml
import shlex


class Context:
    repos: Dict[str, str]
    project_dir: str
    current_branch_name: str


@adhesive.task("Read Current Branch")
def read_current_branch(context: adhesive.Token[Context]) -> None:
    print(f"Running in {context.data.project_dir}")
    context.workspace.pwd = context.data.project_dir

    context.data.current_branch_name = context.workspace.run_output("""
        git rev-parse --abbrev-ref HEAD
    """).strip()


@adhesive.task("Read Configuration")
def read_configuration(context: adhesive.Token[Context]) -> None:
    context.workspace.pwd = context.data.project_dir

    with open("gerepo.yml", "rt") as f:
        config_data = yaml.safe_load(f)

    context.data.repos = dict()
    merge_repos(
        path="",
        repos=context.data.repos,
        data=config_data["mappings"]
    )


@adhesive.task("Pull {loop.value} in {loop.key}")
def pull_image_task(context: adhesive.Token[Context]) -> None:
    if not os.path.isdir(context.loop.key):
        context.workspace.run(f"""
            cd {shlex.quote(context.data.project_dir)}
            git subtree add -P {shlex.quote(context.loop.key)} {shlex.quote(context.loop.value)} master  
        """)

        return


@adhesive.task("Push {loop.value} in {loop.key}")
def push_image_task(context: adhesive.Token[Context]) -> None:
    pass


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
    adhesive.process_start()\
        .branch_start()\
            .task("Read Current Branch")\
        .branch_end()\
        .branch_start()\
            .task("Read Configuration")\
        .branch_end()\
        .task("Pull {loop.value} in {loop.key}", loop="repos")\
        .process_end()\
        .build(initial_data={
        "project_dir": os.path.abspath(os.curdir),
    })


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
