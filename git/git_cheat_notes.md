## Setup Git


| Description            | Command              |
| :-------------------------------------------------------------- |:--------------------------------------------------------------|
| Set up git project| `git init` |
| :-------------------------------------------------------------- |:--------------------------------------------------------------|
| Add everything to WT, ready to commit | `git add .`      |
| Add `path/to/foo` to WT, ready to commit | `git add path/to/foo`      |
| Remove `path/to/foo` from Index/your disk/WT, delete file completely. | `git rm path/to/foo`      |
| Remove path of `path/to/foo` from index,  exclude from the commit. You need this if you have already committed and need to remove a file after adding. the file at wt will be unchanged.  | `git rm --cached path/to/foo`      |
| Commit indexed ommit. You need this if you have already committed and need to remove a file after adding. the file at wt will be unchanged.  | `git rm --cached path/to/foo`      |


| Remove all entries from index and exclude from the commit. You need this if you have already committed and need to remove a file after adding. the file at wt will be unchanged.  | `git reset HEAD`      |
