import sys
import os
import subprocess

# check for directory in REPO_PATH to ensure repo was cloned
# check output of git status if repo is upto date with master.

REPO_PATH: str= "C:\\Repos\\TestForGit"
REPO_URL: str= "https://github.com/Visruat/Coding.git"
REPO_NAME: str= "Coding"
GIT: str= "git"
CLONE: str= "clone"
STATUS: str= "status"
LOG: str= "log"
FETCH: str= "fetch"
PULL: str= "pull"

class Git():

    GIT: str= "git"
    CLONE: str= "clone"
    STATUS: str= "status"
    LOG: str= "log"
    FETCH: str= "fetch"
    PULL: str= "pull"

    def __init__(self):
        self.path = None
        self.url = None
        self.iscloned: bool= False
        self.isgitrepo: bool= False
        self.GIT: str= "git"
        self.CLONE: str= "clone"
        self.STATUS: str= "status"
        self.LOG: str= "log"
        self.FETCH: str= "fetch"
        self.PULL: str= "pull"
        self.CD: str = "cd"
        self.GIT_INIT: str= ".git"

    def CheckForRepo(self, path: str) -> tuple[bool,bool]:
        self.path = path
        try:
            dirs: list= os.listdir(self.path)
        except FileNotFoundError as err:
            self.iscloned = False
            self.isgitrepo = False
            return self.iscloned, self.isgitrepo

        if len(dirs) and self.GIT_INIT in dirs:
            self.iscloned = True
            self.isgitrepo = True
        elif len(dirs) and self.GIT_INIT not in dirs:
            self.iscloned = True
            self.isgitrepo = False
        else:
            self.iscloned = False
            self.isgitrepo = False

        return self.iscloned, self.isgitrepo

    def GitClone(self, url: str, path: str):
        self.url= url
        self.path = path
        input_args: list[str]= [self.GIT, self.CLONE, self.url, self.path]
        process= subprocess.run(input_args, capture_output= True, shell= True)
        return process

def main():
    git = Git()

    is_cloned, is_gitrepo= git.CheckForRepo(os.path.join(REPO_PATH,REPO_NAME))
    if is_cloned and is_gitrepo:
        print(f"Repo: {REPO_NAME} is already cloned!")
    elif is_cloned and is_gitrepo != True:
        raise Exception(f"Repo: {REPO_NAME} is cloned in '{REPO_PATH}' but can't find {git.GIT_INIT}")
    else:
        process= git.GitClone(REPO_URL, os.path.join(REPO_PATH,REPO_NAME))
        print(process)

if __name__ == "__main__":
    main()

