import os.path
import shutil
import subprocess

def git_clone(repo_url, dest, *args):
    a = 'git clone {repo_url} {dest}'.format(repo_url=repo_url, dest=dest).split()
    a.extend(args)
    print('running `%s`' % ' '.join(a))
    try:
        subprocess.check_call(a)
    except:
        # Clean up in case of exception during cloning. This
        # prevents leaving us with a half-populated directory
        if os.path.exists(dest):
            shutil.rmtree(dest)
        raise

def git_update(repo_url, dest, *args):
    a = 'git remote update'.split()
    print('running `%s` on %s' % (' '.join(a), dest))
    subprocess.check_call(a, cwd=dest)

def backup_repos(repos, backup_dir):
    backup_dir = os.path.realpath(os.path.expanduser(backup_dir))
    if not os.path.exists(backup_dir):
        os.mkdir(backup_dir)
        print('created', backup_dir)

    for r in repos:
        repo_name = r['clone_url'].split('/')[-1]
        local_path = os.path.join(backup_dir, repo_name)

        if not os.path.exists(local_path):
            git_clone(r['clone_url'], local_path, '--mirror')
        else:
            git_update(r['clone_url'], local_path)
