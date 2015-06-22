import logging
import os
import shutil
import subprocess

def git_clone(repo_url, dest, *args):
    a = 'git clone {repo_url} {dest}'.format(repo_url=repo_url, dest=dest).split()
    a.extend(args)
    logging.debug('Running `%s`' % ' '.join(a))

    try:
        stdout = subprocess.check_output(a, stderr=subprocess.STDOUT)
    except:
        # Clean up in case of exception during cloning. This
        # prevents leaving us with a half-populated directory
        if os.path.exists(dest):
            shutil.rmtree(dest)
        raise
    else:
        logging.debug(stdout.decode('utf-8').strip())

def git_update(repo_url, dest, *args):
    a = 'git remote update'.split()
    logging.debug('Running `%s` on %s' % (' '.join(a), dest))
    stdout = subprocess.check_output(a, cwd=dest, stderr=subprocess.STDOUT)
    logging.debug(stdout.decode('utf-8').strip())

def backup_repos(repos, backup_dir):
    backup_dir = os.path.realpath(os.path.expanduser(backup_dir))
    if not os.path.exists(backup_dir):
        os.mkdir(backup_dir)
        logging.debug('Created top-level directory', backup_dir)

    for r in repos:
        repo_name = r['clone_url'].split('/')[-1]
        local_path = os.path.join(backup_dir, repo_name)

        if not os.path.exists(local_path):
            git_clone(r['clone_url'], local_path, '--mirror')
        else:
            git_update(r['clone_url'], local_path)
