from setuptools import find_packages, setup

from github_backup import __version__

setup(
    name='github_backup',
    version=__version__,
    license='BSD',
    author='Sam Kingston',
    author_email='sam@sjkwi.com.au',
    description='Script to backup GitHub repositories by mirroring them locally.',
    url='https://github.com/sjkingo/github_backup',
    install_requires=[
        'requests',
    ],
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        github_backup=github_backup.main:main
    """,
)
