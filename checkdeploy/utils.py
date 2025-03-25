import os
import sys
import subprocess

def checkdeploy(ticketArr):
    sys.stdin.reconfigure(encoding='UTF-8')
    sys.stdout.reconfigure(encoding='UTF-8')

    rootDir = "C:\\Users\\friday\\workspace\\bff-nodejs-mobile"
    tickets = ticketArr.split('\r\n')

    # print('rootDir ::', rootDir)
    # print('tickets ::', tickets)

    os.system(f'git --git-dir={rootDir}\\.git fetch > NUL')
    sha1 = subprocess.run(f'git --git-dir={rootDir}\\.git rev-parse origin/master', capture_output=True).stdout.decode('utf-8').replace('\n', '') # master
    sha2 = subprocess.run(f'git --git-dir={rootDir}\\.git rev-parse origin/release', capture_output=True).stdout.decode('utf-8').replace('\n', '') # release
#     print(sha1, sha2)
    commits = subprocess.run(f'git --git-dir={rootDir}\\.git log {sha1}..{sha2} --pretty=format:"%s %an, %ar"', capture_output=True).stdout.decode('utf-8')

    l_commit = []
    for commit in commits.splitlines():
        if commit.find('Merge branch') >= 0:
            continue
        elif commit.find('Web Contents') >= 0:
            continue
        else:
            l_commit.append(commit)

    exists = [] # ticket
    nonExists = [] # ticket

    targets = [] # commit
    nonTargets = [] # commit

    for commit in l_commit:
        bool = False
        for ticket in tickets:
            if commit.find(ticket) >= 0:
                if not ticket in exists:
                    exists.append(ticket)
                bool = True
                break
        if bool:
            targets.append(commit)
        else:
            nonTargets.append(commit)

    for ticket in tickets:
        bool = False
        for exist in exists:
            if ticket == exist:
                bool = True
                break
        if not bool:
            if not ticket in nonExists:
                nonExists.append(ticket)

#     print('exists :: ', exists)
#     print('nonExists :: ', nonExists)
#     print('targets :: ', targets)
#     print('nonTargets :: ', nonTargets)
    return exists, nonExists, targets, nonTargets




