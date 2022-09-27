import os
from pathlib import Path  # noqa: F401

import tomli
from colorama import Fore, init
from invoke import task


@task
def dev(c):
    """run the Flask development server"""
    c.run("python manage.py runserver --host 0.0.0.0", pty=True)


@task
def test(c):
    """run the pytest suite"""
    c.run("pytest", pty=True)


@task(help={"build": "Build images before starting containers."})
def up(c, build=False):
    """docker-compose up -d"""
    if build:
        c.run("docker-compose up -d --build", pty=True)
    else:
        c.run("docker-compose up -d", pty=True)


@task
def exec(c, container, command):
    """docker-compose exec [container] [command(s)]"""
    c.run(f"docker-compose exec {container} {command}", pty=True)


@task
def logs(c, container):
    """docker-compose logs [container]"""
    c.run(f"docker-compose logs {container}", pty=True)


@task
def stop(c):
    """docker-compose stop"""
    c.run("docker-compose stop", pty=True)


@task(
    help={
        "volumes": "Remove named volumes declared in the `volumes` section of the Compose file and anonymous volumes attached to containers."
    }
)
def down(c, volumes=False):
    """docker-compose down"""
    if volumes:
        c.run("docker-compose down -v", pty=True)
    else:
        c.run("docker-compose down", pty=True)


def execute_bump_hack(c, branch):
    """A little hack that combines commitizen-tools and standard-version

    commitizen-tools understands Python stuff, but I don't like the
    generated changelogs. I had no time to look at how to customize them, so I
    decided to use standard-version (from the Javascript world). Unfortunately,
    standard-version doesn't understand Python stuff, and since I didn't have
    time to write my own updater for python files and toml files, I have to
    make the two work together!

    This requires standard-version to be installed globally on your system:
    ``npm i -g standard-version``
    If you're setting it up for the first time on another project, you will probably
    encounter problems generating the entire changelog. See how Łukasz Nojek came up
    with a hack to deal with this:
    https://lukasznojek.com/blog/2020/03/how-to-regenerate-changelog-using-standard-version/

    The formula (workflow) for is as follows:

    1. cz bump --files-only
    2. git add pyproject.toml and other_files specified in pyproject.toml
    3. standard-version --commit-all --release-as <result from cz if not none>
    4. git push --follow-tags origin [branch]

    # TODO: add additional options here, which can passed to either cz or standard version
    """
    print(f"{Fore.MAGENTA}Attempting to bump using commitizen-tools ...{Fore.RESET}")
    c.run("cz bump --files-only > .bump_result.txt", pty=True)
    str_of_interest = "increment detected: "
    result = ""
    with open(".bump_result.txt", "r") as br:
        for line in br:
            if str_of_interest in line:
                result = line
                break
    release_type = result.replace(str_of_interest, "").strip("\n").lower()
    print(f"cz bump result: {release_type}")
    if release_type == "none":
        print(f"{Fore.YELLOW}No increment detected, cannot bump{Fore.RESET}")
    elif release_type in ["major", "minor", "patch"]:
        print(f"{Fore.GREEN}Looks like the bump command worked!{Fore.RESET}")
        print(f"{Fore.GREEN}Now handing over to standard-version ...{Fore.RESET}")
        # first, stage the bumped files
        with open("pyproject.toml", "rb") as f:
            toml_dict = tomli.load(f)
        version_files = toml_dict["tool"]["commitizen"]["version_files"]
        files_to_add = " ".join(version_files)
        c.run(
            f"git add pyproject.toml {files_to_add}",
            pty=True,
        )
        # now we can pass result to standard-release
        print(f"{Fore.GREEN}let me retrieve the tag we're bumping from ...{Fore.RESET}")
        # get_previous_tag = c.run(
        #     "git describe --abbrev=0 --tags `git rev-list --tags --skip=1  --max-count=1`",
        #     pty=True,
        # )
        get_current_tag = c.run(
            "git describe --abbrev=0 --tags `git rev-list --tags --skip=0  --max-count=1`",
            pty=True,
        )
        previous_tag = get_current_tag.stdout.rstrip()
        c.run(
            f'npm run release -- --commit-all --release-as {release_type} --releaseCommitMessageFormat "bump: ✈️ {previous_tag} → v{{{{currentTag}}}}"',
            pty=True,
        )
        # push to origin
        c.run(f"git push --follow-tags origin {branch}", pty=True)
    else:
        print(f"{Fore.RED}Something went horribly wrong, please figure it out yourself{Fore.RESET}")
        print(f"{Fore.RED}Bump failed!{Fore.RESET}")

    # clean up
    c.run("rm -vf .bump_result.txt", pty=True)


@task(help={"fix": "let black and isort format your files"})
def lint(c, fix=False):
    """flake8, black and isort"""

    if fix:
        c.run("black .", pty=True)
        c.run("isort --profile black .", pty=True)
    else:
        c.run("black . --check", pty=True)
        c.run("isort --check-only --profile black .", pty=True)
        c.run("flake8 prayer", pty=True)


# TODO: create a "clean" collection comprising the next two tasks below


@task
def clean_pyc(c):
    """remove Python file artifacts"""

    c.run("find . -name '*.pyc' -exec rm -f {} +", pty=True)
    c.run("find . -name '*.pyo' -exec rm -f {} +", pty=True)
    c.run("find . -name '*~' -exec rm -f {} +", pty=True)
    c.run("find . -name '__pycache__' -exec rm -fr {} +", pty=True)


@task
def clean_test(c):
    """remove test and coverage artifacts"""

    c.run("rm -fr .tox/", pty=True)
    c.run("rm -f .coverage", pty=True)
    c.run("rm -f coverage.xml", pty=True)
    c.run("rm -fr htmlcov/", pty=True)
    c.run("rm -fr .pytest_cache", pty=True)


@task(help={"branch": "The branch against which you wanna bump"})
def bump(c, branch):
    """Use Commitizen Tools & standard-version to bump version and generate changelog

    Run this task when you want to prepare a release.
    First we check that there are no unstaged files before running
    """

    init()

    unstaged_str = "not staged for commit"
    uncommitted_str = "to be committed"
    check = c.run("git status", pty=True)
    if unstaged_str not in check.stdout or uncommitted_str not in check.stdout:
        execute_bump_hack(c, branch)
    else:
        print(f"{Fore.RED}Sorry mate, please ensure there are no pending git operations{Fore.RESET}")


@task
def get_release_notes(c):
    """extract content from CHANGELOG.md for use in Github Releases

    we read the file and loop through line by line
    we wanna extract content beginning from the first Heading 2 text
    to the last line before the next Heading 2 text
    """

    pattern_to_match = "## [v"

    count = 0
    lines = []
    heading_text = "## What's changed in this release\n"
    lines.append(heading_text)

    with open("CHANGELOG.md", "r") as c:
        for line in c:
            if pattern_to_match in line and count == 0:
                count += 1
            elif pattern_to_match not in line and count == 1:
                lines.append(line)
            elif pattern_to_match in line and count == 1:
                break

    # home = str(Path.home())
    # release_notes = os.path.join(home, "LATEST_RELEASE_NOTES.md")
    release_notes = os.path.join("../", "LATEST_RELEASE_NOTES.md")
    with open(release_notes, "w") as f:
        print("".join(lines), file=f, end="")
