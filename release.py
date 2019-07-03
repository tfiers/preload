# Note: on Windows, run with "python release.py --option", i.e. include the
# "python" program explicitly (file associations on Windows 10 suck??).
#
from dataclasses import dataclass
from os.path import exists
from subprocess import run, check_output
from textwrap import dedent
from typing import Sequence

from click import command as CLI, confirm, echo, option, prompt, Abort


@dataclass
class Command:
    args: Sequence[str]
    description: str


@CLI()
@option(
    "-n",
    "--nopoll",
    help="Do not poll for current version number.",
    is_flag=True,
)
@option(
    "-v",
    "--version",
    help="New version number. If not given, will be prompted for.",
)
def release(nopoll: bool, version: str):
    if not exists("setup.py"):
        echo('The current directory does not contain a "setup.py" file')
        raise Abort
    if not nopoll:
        echo("Polling current version number.. ", nl=False)
        output: bytes = check_output(["python", "setup.py", "--version"])
        current_version = output.decode().strip()
        echo(current_version)
    if not version:
        version = prompt("Please enter the new version number")
    commands = (
        Command(
            ("git", "tag", "-a", version, "--message", f"Version {version}"),
            description=(
                f'Create a git tag on the current commit ("-a": include tagger'
                " name, email, date, message, etc)"
            ),
        ),
        Command(
            ("git", "push", "--tags"),
            description="Pushe tags to public source code repository",
        ),
        Command(
            ("python", "setup.py", "sdist", "bdist_wheel"),
            description="Create a source and a built distribution in dist/*",
        ),
        Command(
            ("twine", "upload", "dist/*"),
            description="Upload new distribution to PyPI",
        ),
    )
    for command in commands:
        msg = dedent(
            f"""
            Next command:
                
                {" ".join(command.args)}
            
                Description: {command.description}
            """
        )
        echo(msg)
        if confirm("Execute?", default=True):
            run(command.args)
        else:
            break
    echo("Bye!")


if __name__ == "__main__":
    release()
