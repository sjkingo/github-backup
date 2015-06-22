from setuptools import find_packages, setup
import os.path
import shutil

from github_backup import __version__

# Clear up build dirs first so we don't drag in any old files
for i in ['build', 'dist', 'github_backup.egg-info']:
    if os.path.exists(i):
        print('cleaning', i)
        shutil.rmtree(i)

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
