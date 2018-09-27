
# 1. Terminology

![Git Workflow](https://github.com/aidinhass/ml-cheat-notes/blob/master/images/git_workflow.png)


- remote: The git remote command lets you create, view, and delete connections to other repositories. Remote connections are more like bookmarks rather than direct links into other repositories. 
- Fetch: Download commits, files, and refs from a remote repository into you local repository. You might need this when you want to see what everybody else has been working on.
- Pull: Download content from a remote repository and immediately update the local repository to match that content.

# 2. General

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
| Add a git remote repository | `git remote add -p https://github.com/user/project.git` |
| Push local repository `origin` to remote repository `master`; (set default with `-u`) | `git push -u origin master` |
| Fetch all branches form the remote repository linked | `git fetch`|
| Fetch `bar` branch from `foo` remote repository | `git fetch foo bar`| 
| Fetch from the remote repository linked and merge with the current local repository | `git pull` |
| Fetch from `bar` branch from `foo` remote repository linked and merge with the current local repository | `git pull foo bar` |

 # 3. Collaborate
 
| Description            | Command              |
| :---------------------------------------------------- |:-------------------------------------------------|
| Show remote details| `git remote -v` |
| Show local branches| `git branch` |
| Show remote branches| `git branch -r` |
| Add a git remote repository | `git remote add -p https://github.com/user/project.git` |
| Show all branches| `git branch -a` |
| Create a new branch `foo` | `git branch foo` |
| Switch to branch `foo` and update the working directory| `git checkout foo`|
| Create/Switch to branch `foo` and update the working directory; (create the branch if dose exist with `-b`)| `git checkout -b foo`|
| Merge branch `foo` to the current working directory| `git merge foo`|
| Remove branch `foo`| `git branch -d foo`|

# 4. Undo
TBA

# 5. Collaborative workflow

## 5.1. Centralized
TBA

## 5.2 Feature Branch Workflow:
All feature development should take place in a dedicated branch instead of the master branch.
This encapsulation makes it easy for multiple developers to work on a particular feature without disturbing the main codebase.
It also means the master branch will never contain broken code, which is a huge advantage for continuous integration environments.

The following guideline shows how a user named `<username>` contribute to a project `<projectname>` by creating a new branch to develop `<foo>` feature.
The current setup assumes that the  user`<username>` has benn add to the project collaborators, and he or she has permission to write and modify project contents.
### Set up project repository
1. Clone the the forked repository.
```
git clone git@github.com:<project-creator-username>/<projectname>
```
2. Navigate to the directory of the project repository that you just cloned.
```
mkdir project-ropositroy
cd project-repository
```
### Create new features
1. Start the master branch
- Switch to the master branch
```
git checkout master
```
- Fetch the latest changes from the master branch to match the latest version (HEAD).
```
git fetch origin
git reset --hard origin/master
```
or
```
git pull
```
2. Create/switch a new branch for feature `foo`
```
git checkout -b feature-<foo>/<username>
```
1-2. Implement the two previous steps (1 and 2) with:
 ```
git checkout -b feature-<foo>/<username>
```
3. Implement, change, stage and commit changes:
```
# Implement/Edit/Change
git status
git add <some-file>
git commit -m "<commit-message>"
```

4. Push the feature repository up to the central remote repository.
This can serve as a convenient backup where the user collaborate with other developers.
 This will also give them access to the user's initial commits.
```
git push -u origin feature-<foo>/<username>
```

### Edit existing features
Users can follow the exact same procedure to create a new feature. 

### Publish completed features.
Having a feature completed, a user merges this feature to the project stable branch.

1. Switch to master branch
```
git checkout master
```
2. Pull the latest changes from the master branch
```
git pull
```
3. Pull the latest changes form `feature-<foo>/<username>` branch
```
git pull origin feature-<foo>/<username>
```
This process results in merge commit.
4. Update the project stable with committed and merged changes from `feature-<foo>/<username>`.
```
git push
```

# 6. Commit message convention

1. Imperative form
2. Capitalized
3. No longer than 50 characters
4. Not end with periods

Examples:
- Add 'README.md'
- Fix login bug
- Correct typo
- Add plot function
- Comment data module
- Remove unused files

# 7. Branch naming convention

1. **`master`**: a master branch for final release
2. **`develop`**: a branch off of master branch for most main-line development works.
3. **`feature-<feature-name>/<user-name>`**: multiple branches off of the develop branch.
(**`<feature-name>`**: name of feature; **`<user-name>`**: person working on the feature)
4. **`release`**: a branch as a candidate release
5. **`hotfixes`**: short-lived branches for changes to apply to the master branch

![Git Workflow](https://github.com/aidinhass/ml-cheat-notes/blob/master/images/git_model.png)

# References
- [A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)



