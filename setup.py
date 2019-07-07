from setuptools import setup, find_packages


GITHUB_URL = "https://github.com/tfiers/preload"

setup(
    name="preload",
    description="Give feedback to user while program hangs at start",
    license="MIT",
    author="Tomas Fiers",
    author_email="tomas.fiers@gmail.com",
    url=GITHUB_URL,
    project_urls={"Source Code": GITHUB_URL},
    packages=find_packages(),
    use_scm_version=True,  # Get package version from git tags.
    setup_requires=["setuptools_scm"],
)
