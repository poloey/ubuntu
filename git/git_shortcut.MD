### for status
~~~
git status
~~~

### to add file to git 
~~~
git add .
~~~

### to pull a branch
~~~
git pull origin <branch>
~~~

### to chckout branch 
~~~
git checkout <branchName>
~~~

### to reset the changed file as like branch
~~~
git checkout .
~~~

### to commit
~~~
git commit -m "<message>"
~~~

### to push 
~~~
git push origin <branch name>
~~~

### to pull all branch
~~~
git fetch --all
~~~

### to change url in git 
~~~
git remote set-url origin <link>
~~~
### 
~~~
git clean -f -d
~~~

### to clone only last build or some thing
~~~
git clone --depth 1 <git url>
~~~
### to know remote git url - kind of checking version in case of other app
~~~
git remote -v
~~~

### in .gitignore ignore certain file type
~~~
*.json
!spec/*.json   
~~~


### to set new remote
~~~
git remote set-url origin <new git url>
~~~

### to push all branches
~~~
git pull --all
~~~

### to know all origin and git remote url 
~~~
git remote show origin
~~~

### seeing git diff
~~~
git diff HEAD^^^^
~~~

### mistakenly i pulled wrong buched. following code save my day
~~~
git reflog show  - that will show all previous commit HEAD
git reset HEAD@{2} - that will reset the HEAD
~~~

### to fix case in sensitivity in windows and mac following command is needed
~~~
git config core.ignorecase false
~~~


### to delete untracked file and folder in git.  To clean to origin ???? normally if you type git checkout . it will checkout to current origin but all untracked file will be remain. in order to delete untracked file you have to type following command
~~~
git clean -f -d
~~~

### add git url to existing project
~~~
git remote add origin <url>
~~~

### change git url 
~~~
git remote set-url origin <url>
~~~

### to create a branch
~~~
git checkout -b <branch name>
~~~

### to delete a branch
~~~
git branch -d <branch name>
~~~


### setting
~~~
git config --global user.name "Polo Dev"
git config --global user.email polodev10@gmail.com
~~~

###update   
~~~
git config --replace-all user.email "new@mail.com"
git config --replace-all user.name "new name"
~~~

### getting
~~~
git config --global user.name 
git config --global user.email 
~~~



