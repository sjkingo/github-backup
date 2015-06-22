#!/usr/bin/env python3

import argparse
import json

import os.path, sys
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

from github_backup.api import *
from github_backup.git import backup_repos

DEFAULT_DIR = '~/.github-bkp'

def parse_args():
    parser = argparse.ArgumentParser(description='Script to backup GitHub repositories by mirroring them locally')
    parser.add_argument('username', help='The GitHub username to back up')
    parser.add_argument('-d', dest='backup_dir', default=DEFAULT_DIR,
            help='Directory to back up to (defaults to %s)' % DEFAULT_DIR)
    parser.add_argument('-m', dest='meta_only', action='store_true',
            help='Don\'t mirror repositories; instead dump their metadata to stdout')
    return parser.parse_args()

def dump_metadata(repos):
    j = json.dumps(repos, indent=2)
    print(j)

def main():
    args = parse_args()
    r = get_repos_for_user(args.username)
    if args.meta_only:
        dump_metadata(r)
    else:
        backup_repos(r, args.backup_dir)


if __name__ == '__main__':
    main()
