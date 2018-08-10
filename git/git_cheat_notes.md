
## Terminology

![Git Workflow](https://github.com/aidinhass/ml-cheat-notes/blob/master/images/git_workflow.png)


- Fetch: Download commits, files, and refs from a remote repository into you local repository. You might need this when you want to see what everybody else has been working on.
- Pull: Download content from a remote repository and immediately update the local repository to match that content.

## General

| Description            | Command              |
| :---------------------------------------------------- |:-------------------------------------------------|
| Set up git project| `git init` |
| Add everything to SA, ready to commit | `git add .`      |
| Add `path/to/foo` to SA, ready to commit | `git add path/to/foo`      |
| Remove `path/to/foo` from WD/SA/LR. Delete file completely. | `git rm path/to/foo`      |
| Remove path of `path/to/foo` from SA, exclude from the commit. You need this if you have already committed and need to remove a file after adding. The file at LR will be unchanged after commit. You might also need if you want remove a file from LR but keep you copy at WD.  | `git rm --cached path/to/foo`      |
| Move or rename `path/to/foo` to`path/to/bar` | `git mv path/to/foo path/to/bar`  | 
| Commit staged files. | `git commit -m "Commit message in imperative form"`      |
| Add and Commit in a single step | `git commit -am "Commit message in imperative form"` |
| Add a git RR | `git remote add -p https://github.com/user/project.git` |
| Push local repository `origin` to remote repository `master`; (set default with `-u`) | `git push -u origin master` |
| Fetch all branches form the remote repository linked | `git fetch`|
| Fetch the `bar` branch from the `foo` remote repository | `git fetch foo bar`| 
| Pull from the remote repository linked and merge with the current local repository | `git pull` |

 ## Collaborate
 
| Description            | Command              |
| :---------------------------------------------------- |:-------------------------------------------------|
| Show remote details| `git remote -v` |
| Show local branches| `git branch` |
| Show remote branches| `git branch -r` |
| Show all branches| `git branch -a` |
| Create a new branch `foo` | `git branch foo` |
| Switch to `foo` branch and update the working directory| `git checkout foo`|
| Create/Switch to `foo` branch and update the working directory; (create the branch if dose exist with `u`)| `git checkout foo`|
| Merge the `foo` branch to the current working directory| `git merge foo`|
| Remove the branch `foo`| `git branch -d foo`|

## Undo

| | |

## Collaborative workflow:

### Centralized
1. Initialize the central master branch:

- Switch to the master branch
```bash\
git checkout master
```
- Fetch the latest changes from the 

### Feature Branch Workflow:
All feature development should take place in a dedicated branch instead of the master branch.
This encapsulation makes it easy for multiple developers to work on a particular feature without disturbing the main codebase.
It also means the master branch will never contain broken code, which is a huge advantage for continuous integration environments.


1. Create a new branch to work on. 
```shell
git branch 
 ```