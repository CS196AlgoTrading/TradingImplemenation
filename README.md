# CS 196 Spring 2017 Algorithmic Trading Platform

## Overview

This project is currently broken up into three parts:

  * **Listener** - polls the Yahoo Finance API and outputs the data
  * **Streamer** - reads from a file and exposes the data as Python objects or primitives
  * **Models** - makes models using market data

The parts are generally connected like this:

**Listener** -> **Streamer** -> **Models**

## Installation and Usage

  * Install python 3.5+
  * Install pip
    * Download [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py) (`wget https://bootstrap.pypa.io/get-pip.py`)
    * Run the get-pip.py with python3 (`sudo python3 get-pip.py` on most setups)
  * Clone this repository
    * `git clone https://github.com/CS196AlgoTrading/trading-platform`
  * Install the requirements for this project
    * Navigate into the trading-platform/ directory (`cd trading-platform`)
    * `sudo pip3 install -r requirements.txt`
  * Install the project
    * If you are a developer or plan to modify the project
      * `sudo python3 setup.py develop`
    * If you do not plan to modify the project
      * `sudo python3 setup.py install`

## Git Version Control

This project uses [git](https://github.com/git/git).

### Quick Reference

| Command                        | Description                                                                         |
| ------------------------------ | -----------------------------------------                                           |
| `git branch`                   | list the branches and show the current branch                                       |
| `git branch BRANCH-NAME`       | create a new branch with the name BRANCH-NAME                                       |
| `git checkout BRANCH-NAME`     | checkout the branch named BRANCH-NAME                                               |
| `git add FILENAME`             | add a file to *staging*                                                             |
| `git commit -m "some message"` | bundle all the files in staging into a new commit (a new version of the branch)     |
| `git push origin BRANCH`       | pushes the current branch (on your computer) to the GitHub server hosting our repo  |
| `git fetch origin`                    | download the latest version of the repo, but don't change the code on your computer |
| `git merge origin/BRANCH`      | merge the fetched code into your local working copy of the repo                     |


### Quick Workflow Reference

  1. Checkout master: `git checkout master`
  2. Get the latest changes from GitHub: `git fetch origin`
  3. Merge the latest version of master into my local version of master: `git merge origin/master`
  4. Create a new branch for the code I will write: `git branch my-new-feature`
  5. Checkout the branch: `git checkout my-new-feature`
  6. Write the code that implements the feature to be added
  7. See which files I changed and added: `git status -s`
  7. Add each file *individually* to the staging area:
    * `git add some_file_that_I_made.py`
    * `git add some_other_file_I_changed.py`
  8. Commit all of the files in staging: `git commit -m "add my-new-feature blah blah"`
    * this makes a new version of the codebase based on all the files in staging
  9. Push (upload) my new commit (version) to GitHub: `git push origin my-new-feature`


### Example Workflow

This is an example of using git as a developer of this project. In this example, I will add code to this project that completes the **Listener** part.

First, I need to download the latest copy of *master* --- the main branch of our codebase --- from GitHub to my computer. I will checkout *master*, download the latest version, and then merge the latest version of *master* with my version of *master*.

```
$ git checkout master      # checkout the master branch on my computer
$ git fetch origin         # download the latest code from GitHub, but don't modify the code on my computer
$ git merge origin/master  # "merge" the latest version of master into my local working version of master
```

Then, I need to checkout the *branch* that I will work on.

```
$ git checkout listener
error: pathspec 'listener' did not match any file(s) known to git.
```

The command failed since the `listener` branch doesn't exist yet. Since it doesn't exist, I need to create it.

```
$ git branch listener
```

To see which branch I'm currently on, I can run `git branch` without any arguments:

```
$ git branch
listener
* master
```

The output shows that there are two branches: `master` and `listener`. The asterisk next to master indicates that `master` is currently checked out.

I need to checkout `listener`, since I'll be working on that.

```
$ git checkout listener
```

This time it succeeded. Now I write the code that implements the **Listener** part of the platform.

Now that I'm finished writing code, I need to *push* my version of code to *origin*. Pushing code essentially means to upload it somewhere. In this case, we push the code to *origin*, which is an alias for a server owned by GitHub. It is possible to see the actual address of the server:

```
$ git remote -v
origin	git@github.com:CS196AlgoTrading/TradingImplemenation.git (fetch)
origin	git@github.com:CS196AlgoTrading/TradingImplemenation.git (push)
```

The output shows that *origin* actually points to `git@github.com:CS196AlgoTrading/TradingImplemenation.git`. However, this is not particularly important. What I need to do is create a new commit --- a new version of the code in this repository --- which has all my code, and then push that commit to origin. First, I'll see which files I've actually created or changed.

```
$ git status -s
 M README.md
 M tradingplatform/__init__.py
 M tradingplatform/listener.py
```

The output of `git status -s` shows that I've modified `README.md`, `tradingplatform/__init__.py` and `tradingplatform/listener.py`. I should add all of those files with `git add`:

```
$ git add README.md
$ git add tradingplatform/__init__.py
$ git add tradingplatform/listener.py
```

It is also possible to add files with pattern matching (for example, `git add *`, which matches all files), but this is **strongly discouraged**. It is very easy to accidentally add files that shouldn't be added when adding more than one file at a time. So it is best to simply `git add` each individual file.

Now that the files have been added, I need to turn all of the added files into one *commit* --- one version --- of our repository.

```
$ git commit -m "add listener"
```

A message which describes the commit is specified with the `-m` flag. It is best to **always use present tense** in the first line of commit messages. For example, prefer `git commit -m "fix bug #1337"` over `git commit -m "fixed bug #1337"`.

Finally, push this commit to *origin* --- the GitHub server which contains this repository. I make sure to push my changes to the branch that I'm on as well:

```
$ git push origin listener # origin is 'where', listener is 'which branch'
```

