import environ
import os
import sys
import requests
import json

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

def checkdeploy(ticket_arr):
    sys.stdin.reconfigure(encoding='UTF-8')
    sys.stdout.reconfigure(encoding='UTF-8')

    tickets = ticket_arr.split('\r\n')

    # print('rootDir ::', rootDir)
    # print('tickets ::', tickets)
    private_token = env('PRIVATE_TOKEN')
    gitlab_api_server = env('GITLAB_API_SERVER')

    master = requests.get(f'{gitlab_api_server}/repository/branches/master', headers={'PRIVATE-TOKEN': private_token})
    sha1 = json.loads(master.text)["commit"]["id"]

    release = requests.get(f'{gitlab_api_server}/repository/branches/release', headers={'PRIVATE-TOKEN': private_token})
    sha2 = json.loads(release.text)["commit"]["id"]

    diff = requests.get(f'{gitlab_api_server}/repository/compare?from={sha1}&to={sha2}', headers={'PRIVATE-TOKEN': private_token})

    commits = []
    for commit in json.loads(diff.text)["commits"]:
        if commit['title'].find('Merge branch') >= 0:
            continue
        elif commit['title'].find('Web Contents') >= 0:
            continue
        else:
            commits.append(commit['title'])

    exists = [] # ticket
    non_exists = [] # ticket

    targets = [] # commit
    non_targets = [] # commit

    for commit in commits:
        is_target = False
        for ticket in tickets:
            if commit.find(ticket) >= 0:
                if not ticket in exists:
                    exists.append(ticket)
                is_target = True
                break
        if is_target:
            targets.append(commit)
        else:
            non_targets.append(commit)

    for ticket in tickets:
        is_exist = False
        for exist in exists:
            if ticket == exist:
                is_exist = True
                break
        if not is_exist:
            if not ticket in non_exists:
                non_exists.append(ticket)

#     print('exists :: ', exists)
#     print('non_exists :: ', non_exists)
#     print('targets :: ', targets)
#     print('non_targets :: ', non_targets)
    return exists, non_exists, targets, non_targets




