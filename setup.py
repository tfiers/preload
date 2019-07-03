from setuptools import setup, find_packages

setup(
    name="preludio",
    description="Give feedback to user while program hangs at start",
    author="Tomas Fiers",
    author_email="tomas.fiers@gmail.com",
    project_urls={"Source Code": "https://github.com/tfiers/preludio"},
    packages=find_packages(),
    use_scm_version=True,  # Get package version from git tags.
    setup_requires=["setuptools_scm"],
)
