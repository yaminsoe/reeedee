from logging import FileHandler, StreamHandler, INFO, basicConfig, error as log_error, info as log_info
from os import path as ospath, environ, execl as osexecl
from subprocess import run as srun
from requests import get as rget
from dotenv import load_dotenv
from sys import executable

if ospath.exists('botlog.txt'):
    with open('botlog.txt', 'r+') as f:
        f.truncate(0)

basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[FileHandler('botlog.txt'), StreamHandler()],
                    level=INFO)

UPSTREAM_REPO = environ.get('UPSTREAM_REPO')
UPSTREAM_BRANCH = environ.get('UPSTREAM_BRANCH')
try:
    if len(UPSTREAM_REPO) == 0:
       raise TypeError
except:
    UPSTREAM_REPO = "https://github.com/khainee/render-mltb"
try:
    if len(UPSTREAM_BRANCH) == 0:
       raise TypeError
except:
    UPSTREAM_BRANCH = 'beta'

if ospath.exists('.git'):
    srun(["rm", "-rf", ".git"])

update = srun([f"git init -q \
                 && git config --global user.email khingzay797@gmail.com \
                 && git config --global user.name khainee \
                 && git add . \
                 && git commit -sm update -q \
                 && git remote add origin {UPSTREAM_REPO} \
                 && git fetch origin -q \
                 && git reset --hard origin/{UPSTREAM_BRANCH} -q"], shell=True)

if update.returncode == 0:
    log_info('Successfully updated with latest commit from UPSTREAM_REPO')
    log_info(f'Upstream Repo: {UPSTREAM_REPO}')
    log_info(f'Upstream Branch: {UPSTREAM_BRANCH}')
else:
    log_error('Something went wrong while updating, check UPSTREAM_REPO if valid or not!')
    log_info(f'Entered Upstream Repo: {UPSTREAM_REPO}')
    log_info(f'Entered Upstream Branch: {UPSTREAM_BRANCH}')

