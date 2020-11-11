import subprocess

from termcolor_util import yellow, green

from git_monorepo.git_monorepo_config import (
    read_config,
    write_synchronized_commits,
    get_current_commit,
)
from git_monorepo.git_util import is_repo_unchanged
from git_monorepo.pull_command import env_extend


def push(resync: bool):
    monorepo = read_config()

    for folder_name, repo_location in monorepo.repos.items():
        if is_repo_unchanged(monorepo, folder_name) and not resync:
            print(
                green(repo_location, bold=True),
                green("->"),
                green(folder_name, bold=True),
                green("UNCHANGED", bold=True),
            )
            continue

        print(
            yellow(repo_location, bold=True),
            yellow("->"),
            yellow(folder_name, bold=True),
            yellow("PUSH", bold=True),
        )

        initial_commit = get_current_commit(project_folder=monorepo.project_folder)

        subprocess.check_call(
            [
                "git",
                "subtree",
                "push",
                "-P",
                folder_name,
                repo_location,
                monorepo.current_branch,
            ],
            cwd=monorepo.project_folder,
            env=env_extend(
                {
                    "EDITOR": "git-monorepo-editor",
                    "GIT_MONOREPO_EDITOR_MESSAGE": f"git-monorepo: push {folder_name}",
                }
            ),
        )

    current_commit = get_current_commit(project_folder=monorepo.project_folder)

    # we need to update the last commit file with the new value
    # the commit is the current_commit, since this is already pushed
    write_synchronized_commits(monorepo, repo=folder_name, commit=current_commit)
