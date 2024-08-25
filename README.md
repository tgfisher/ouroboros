# ouroboros  :snake:

Learn to write code, store code, and share code.

Have fun and ask someone before beating your head against a wall.

This is a living document. Check back in occasionally to see updates.

The heart of this document for new python users are the `notebooks`, specifically [the interactive tutorial][ln_interactivetutorial].

### Table Of Contents
1. [An Introduction to Python](#an-introduction-to-python-nerd_face)
    - [Python Installation](#python-lesson-1-python-installation-cowboy_hat_face)
    - [Virtual Environments](#python-lesson-2-virtual-environments-disguised_face)
    - [Python Basics \& Jupyter](#python-lesson-3-python-basics--jupyter-astronaut)
    - [Anatomy of a Package](#python-lesson-4-anatomy-of-a-package)
    - [Installing a Local Package](#python-lesson-5-installing-a-local-package)
1. [Version Control: Git \& GitHub.com](#version-control-git--githubcom-octocat)
    - [Analogy to "tracking changes"](#git-lesson-1-version-control-a-tracking-changes-analogy-bowtie)
    - [Getting Git](#git-lesson-2-git-setup-and-first-steps-hugs)
    - [Git Comfortable (Basic Usage)](#git-lesson-3-git-comfortable-woman_technologist)
    - [The `git` GitHub.com relationship](#git-lesson-4-the-git-github-relationship)

# About This Repo

A modern scientific computing workflow utilizes a broad set of tools and
techniques: programming languages, algorithms, statistical learning, version
control, &c. It is easy to get bogged down in the details and forget that these
tools are (for the most part) a means to a scientifically relevant end.

This README.md will guide you through python3-based scientific computing
concepts. If it is your first time going through it, take your time, trust the
process, and go in order. Along the way you will learn `python3` coding basics
such as syntax and common packages like `numpy`, but our real focus is on to show 
the supporting fundamentals which are often learned piecemeal or too late. These
fundamentals can be hard to learn because they aren't as googleable
as code snippets or packages of tools. If you are a bit fuzzy on the basics (e.g.
environments, imports, versions, &c.) or you are new to scientific
computing with `python3` this content should put you on track to improve your skills
and empower you to more easily improve your own skills.

It is important to mention that this content aims to 'teach a person to fish',
rather than 'give a person a fish'. Not every concept will receive an explicit
didactic breakdown. **Advanced tricks and syntax will be sprinkled throughout
this tutorial. These should be seen as opportunities for growth and serve to
expose the reader and encourage them to dive a bit deeper.**  If you would like
to learn more about any of the concepts we raise there are so many GREAT
resources such as [RealPython.com][ln_RealPython_home], ['Learn Python the Hard
Way'][ln_learnpythonthehardway], and [CS106A][ln_programmingmethods].

Additionally, the format of this _repository_ is a bonus; it stands as an
example (or 'template') for _packaging_ your own python code in a `pip
install`-able format and tracking it using `git` and GitHub. Organizing code
into a [python package][ln_RealPython_packages] _<--you don't have to read all
that now, but it is an example of a [RealPython.com][ln_RealPython_home]
resource_, and
storing them using GitHub, will save you a lot of headaches in the future. This
template can be reused as a scaffold; replace our stuff with your
stuff to make a `pip`-installable package of your own. We will explain that in
more detail later.

:disappointed: If you just [NEED TO LEARN PYTHON NOW][ln_python_colab] you can establish yourself
as a python user without any of the foundational concepts. _(not recommended)_

**Originally produced for Giocomo Lab rotation labbies by Linnie Jiang and Tucker Fisher**.

_remember us when you are famous._ [:woman_technologist:][ln_linnie_twitter] [:man_mechanic:][ln_tucker_home]

## First Things First :bread: 'n :butter:

- [ ] Setup [your bash terminal][ln_CNJCx_terminalsetup] by following along in the "Prerequisites section".
    - When you have time check out [CNJCx course][ln_CNJCX_home] for a deeper dive on many topics not covered in this tutorial: vim, tmux, ssh, Windows Subsystem for Linux, &c.
- [ ] Choose a text editor you like ([VS Code][ln_vscode_dl], [Atom][ln_atom_dl], and [Sublime][ln_sublime_dl] are all good options)
- [ ] \[**GitHub.com users**\] Clone this repository onto your local machine.
- [ ] \[**Everyone else**\] Download this repository onto your local machine.
    - Select the green <kbd>code v</kbd> button where you can download [the zip][ln_zip_of_repo].
    - Don't worry about getting GitHub.com proficient until [the section on git](#version-control-git--githubcom-octocat).

---
---

# An Introduction To Python :nerd_face:

**Learning Goals  :anchor:**
- [ ] Grasp the distinction between **python versions** (e.g. `python3` vs `python` vs. `python2.7` &c.).
- [ ] Understand that you can have multiple **python executables** for the same--or different--python version (e.g.<br/>`/usr/bin/python3`&nbsp;<--&nbsp;_could be version 3.8.1_ while `/usr/local/bin/python3`&nbsp;<--&nbsp;_could be version 3.9.0_).
- [ ] Use a **virtual environment** and know _when_ to use them.
- [ ] _Bonus: Grasp the mechanics of how a virtual environment works._
- [ ] `pip install`-ing packages, or "tools", into your virtual environment, or "workshop".
- [ ] _Basic Usage_: numpy
- [ ] _Basic Usage_: jupyter
- [ ] _Basic Usage_: matplotlib --> how to plot the ["right"](#what-does-right-or-correct-mean) way.
- [ ] Choosing a text editor and setting up a development environment.
- [ ] `pip install`-ing **your custom packages**
- [ ] _Basic Usage_: `git`


## Python Lesson 1: Python Installation :cowboy_hat_face:

The trick to installing python ["correctly"](#what-does-right-or-correct-mean)
is _understanding what you are doing, and knowing where python goes after
installation_. This might sound silly, but with so many Stack Overflow entries
and blogs, you might have python... but not really understand how you got it.
this might come back to bite you because there are a ton of different versions
and "types" of python and they can share names (e.g. `python`, `python3`,
`python3.9`, `pythonw`).

### Step 1: Get Oriented

If you are on macOS or Ubuntu, WSL included, your OS relies on python for some scripts.
_Likely_ you have python2.7. Most Ubuntu and macOS installs should come with
a "python" that is version 2.7. _This might not be true anymore, your system likely
ships with `python3` now!_

The `which` command at the bash/zsh command line tells you what the computer would do if
you ran that command. If you want to know what `python` does you can run `which`.

```bash
which python # this is a comment, bash ignores things after '#'
```

Additionally, the `-a` **flag**, flags are options on bash functions, will list all
the instances of executables found associated with a command. The computer searches
for a command in various locations (in the order they appear in your `PATH` variable).
You can run `echo $PATH` to see your paths and their order.

```bash
which -a python3 # check out which python3 you have lying around
``` 

### Step 2: Get Python

|| [macOS](#macos-instructions) || [Ubuntu (and Windows
Subsystem for Linux)](#ubuntu-and-windows-subsystem-for-linux) || 

#### macOS Instructions<a name="first-lesson-macos"></a>

_These installation instructions are adapted from [CNJCx Practical
Python][ln_CNJCx_home] courtesy of [Eshed Margalit][ln_Eshed_home]._

You might need `$ xcode-select --install`.

[Homebrew][ln_Homebrew_home] is a great way to get and manage packages on MacOS
and we are going to use it to get python&nbsp;_<--&nbsp;in&nbsp;this&nbsp;case
'packages' doesn't mean 'python packages', `brew` manages all kinds of software
packages_.  Installing it is easy, you should have taken care of it in the
[First Things First](#first-things-first-bread-n-butter) section:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Getting the newest stable version of python is an easy one-liner with `brew`

```bash
brew install python3 # if you get an "already installed error" try `brew upgrade python@3.9`
```

Q: Where did it install? 

A: We can check using `brew --prefix`. This commands returns the default
install path for brew.

```bash
brew --prefix # this command-flag-pair tells you where `brew` puts things
/usr/local
```

This means our new python lives at `/usr/local/bin/python<version>`. By
convention directories called `bin` contain "binaries", or compiled source
code. Executables are also commonly placed in `bin` directories.  We've
put in "\<version\>" as a placeholder for the _version_ since it could be 3.6,
3.8, or 3.9 depending on what you have downloaded. 

To use _this brewed_ python you need to use that whole path, otherwise it will
use the first python in the `$ which -a python`. Luckily there is a trick we
can use to bring our new python to the front of the line. This trick is the
`alias` command in bash.

```bash
alias brewedpython='/usr/local/bin/python3'
```

Now try `which`

```bash
which brewedpython
```

#### Ubuntu (and Windows Subsystem for Linux)<a name="first-lesson-ubuntu"></a>

We don't need an external package manger for Ubuntu because it isn't missing (like
it is on macOS). _This will depend on your Ubuntu release. Possible that `deadsnakes` isn't 
necessary. TODO: recommend install from python directly?_

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.9
sudo apt-get install python3.9-venv
```

Now try `which`

```
which -a python3.9
```
## Python Lesson 2: Virtual Environments :disguised_face:

Virtual environments are like workshops. A blacksmith shop is quite different
than of a furniture maker. The two disciplines have specialized tools for
specialized uses. Critically for this metaphor, their raw materials, tools, and
equipment might not mix. For example, having sawdust and dry wood scattered
about would be pretty dangerous when sparks are flying.

With python there is a potential for some pieces of software to conflict like
this. Using virtual environments puts you in control; your workshop only has
what you need for a particular project and this will help prevent conflicts.

Under the hood, when you **activate** your virtual environment the commands and
paths that define it are placed at the top of your PATH until you
**deactivate**. Run `echo $PATH` before (and then, after) you've activated the
environment and you will see for yourself.

#### Making A Virtual Environment

The `venv` module contains code that makes virtual environments. _A
[module][ln_about_modules] is a `.py` file that contains reusable python code
structured such that it can be imported or used elsewhere. This is in contrast
to code that is only available from within a file, like the code in a script._
Using the module flag `-m` with `venv` looks like this: `python<version> -m
venv </path/to/your/new/env>`._

```bash
python3.9 -m venv ~/we_sick_venv
    --- OR if you made an alias above ---
brewedpython -m venv ~/we_sick_venv
```

Wow, you just made a virtual environment! :eyes:

```bash
source ~/we_sick_venv/bin/activate
(we_sick_venv) $ # the prompt changes to tell you what venv you are in
```

#### Stocking your Virtual Environment with Packages (Tools)
 
`pip` (**p**ip **i**nstalls **p**ackages)

```bash
(we_sick_venv) $ pip list # shows you what you have installed
(we_sick_venv) $ pip install numpy # numpy is #1, it is the most important package
(we_sick_venv) $ pip install matplotlib # this is a plotting library
(we_sick_venv) $ pip install jupyter # ppl with matlab experience might appreciate this tool
(we_sick_venv) $ pip install ipykernel # we need this to do a cool jupyter trick later
```

## Python Lesson 3: Python Basics \& Jupyter :astronaut:

_Disclaimer: Jupyter can create bad habits (long and confusing asynchronous scripts), but it
is powerful when properly deployed and is a nice way to show python in action._

#### Starting Jupyter From the Command Line

Now that we have python, and we have a virtual environment to play in, lets start
jupyter and begin to `code`!! 

`cd` into the top-level of the ouroboros directory before
running the commands below.

```bash
cd /path/to/ouroboros
ls # you should see something like what is listed below
README.md    bin    notebooks    ouroboros    pyproject.yaml
```

Once you know that you are in the right place we can fire up jupyter. There are
a few ways to do this. If you are a first-timer just run the classic `jupyter notebook`.

```bash
(we_sick_venv) $ jupyter notebook
    --  OR  --
(we_sick_venv) $ jupyter notebook --no-browser # if you dont want a browser
    --  OR  --
(we_sick_venv) $ jupyter notebook --port=4343 # if you don't want to use the default 8888
       #===  don't panic, a ton of stuff will pop up here ===#
```

Visit the `giocomo_python_tutorial.ipynb` by clicking through the directory
structure, this file is in the `notebooks` directory off of the `ouroboros` top
level directory.  Running the cells from this notebook in order should expose
you to a bunch of basic python and numpy.

![Screen Shot 2022-12-09 at 1 28 33 PM](https://user-images.githubusercontent.com/26031420/145478775-3eb36b5a-2c98-4800-9485-39925eb1c3ba.png)

#### Jupyter Kernels (Bonus, more advanced)

To run the juptyer using your virtual environment, you must first activate your
environment and then start jupyter. Is there a way to just start jupyter and
have all of your virtual environments ready for you? **YES!!**

```bash
(we_sick_venv) $ deactivate
which python3 # you aren't in your workshop anymore (we want that)
python3 -m pip install jupyter # note this is putting jupyter randomly in your "home" python
```

If you run `jupyter notebook` now, you will be using the "home", or **base**,
python.  It won't have any of the tools that you need from your virtual
environment. We are going to teach you _a trick_ that is convenient if you have
many virtual environments and use jupyter notebooks for development.

```bash
jupyter notebook
       #===  as always a ton of stuff will pop up here ===#
```

Notice that the kernels that you have available to you are limited--you might
only have one. We can add all of our virtual environments into one place and
make them super convenient. We will be able to get to all of them without even
having to activate them.

```bash
source we_sick_venv/bin/activate
(we_sick_venv) $ python -m ipykernel install --name=we_sick_venv --display-name="Python (we_sick_venv)"
(we_sick_venv) $ deactivate
jupyter notebook
       #===  don't panic, a ton of stuff will pop up here ===#
```

Like magic, your venv is now available. Make another venv and add it to the
kernels, it will be there too.

<div align="center">
<img
src="https://user-images.githubusercontent.com/26031420/145482739-bf25925c-0555-4075-89db-7797b7331d1b.png" 
width="40%"
title="Using the 'New button' shows a the 'Python (we_sick_venv)' kernel available."
/>
</div>


### Python Lesson 4: Anatomy of a Package

#### Anatomy of a python package

```bash
your_package_name # This is the root of your project (the name of the repo) and is most often <your_package_name>.
 │
 ├── README.md # This .md ('markdown' file) is an ideal place to put information about your
 │             # repository: what it does, how to install it, &c. As a bonus GitHub.com
 │             # automatically shows these contents on the repo's landing page.
 │
 ├── bin # Not required, this is a good place to put scripts 'scripts' is and equally good directory name.
 │   │
 │   └── a_sript.py # scripts are useful standalone chunks of code (e.g. a preprocessing script).
 │                  # A mature jupyter notebook could be a good script candidate. Google
 │                  # sys.argv if you would like to add 'inputs' to a script.
 │
 ├── notebooks/ # Not required, this is where you can store notebooks. 
 │   │
 │   └── a_notebook.ipynb # Notebooks are block style asynchronous scripts. They are a great for
 │                        # developing your package and performing analysis with visualizations.
 │                        # They can also be very powerful as living documentation, and can provide
 │                        # provide explicit usecase examples for package features.
 │
 ├── src
 │   │
 │   └── your_package_name/ # This top-level directory (the package) commonly has the same name as the repo root.
 │       │
 │       ├── __init__.py # This file is often empty, but it can control import flow of modules
 │       │               # and sub-packages under it in the directory structure. Note: that in the
 │       │               # most recent python versions packages don't 'require' the empty __init__.py.
 │       │
 │       ├── a_module.py # Modules are where reusable code chunks are stored: functions, classes,
 │       │               # variables. Modules can also contain scripts under `if __name__ == "__main__:"`
 │       │               # __name__ will be "__main__" when the module is run as a script:
 │       │               # `python a_module.py` <-- from the command line.
 │       │
 │       └── a_subpackage/ # A subpackage helps to further specify your package namespace.
 │           │
 │           ├── __init__.py # Again, it is common for a package to have this, even if it is empty.
 │           │
 │           └── a_module.py # We've used the same module name as above but, critically,
 │                           # it has a different import path. This means the two names will
 │                           # not collide: `your_package_name.a_module` versus
 │                           # `your_package_name.a_subpackage.a_module`.
 │
 └── pyproject.yaml # This file is critical for making your package `pip install`-able 
                    # Note: there isn't 'one way' to do it. The pyproject file included in this
                    # repository is an example of a fairly simple, but decently featured
                    # pyproject file. The pyproject.yaml file example should be more than enough for
                    # most situations.
```

### Python Lesson 5: Installing a Local Package

#### Local Package Install Command

```bash
pip install -e . # if you are in the project directory
    --- OR ---
pip install -e <path/to/your/package/root> # if you aren't currently in the project direcory.
```
#### Contextualizing the Local `pip install`

This repository is setup as a package. It has all the necessary components to
be simply 'pip install'-ed into a virtual environment. The difference between
installing a package like "numpy" and installing your local package is quite small:

1) You will make changes to your package during development. Unlike the packages
you might download from the [Python Package Index (PyPI)][ln_pypi] (e.g. numpy,
matplotlib, jupyter), your local code will constantly evolve as you move 
forward in your project. Adding the `-e` for "editable" sets up the install
to check your package source code for updates whenever the package is used.

2) Another difference is where you point pip to install. Looking into the
documentation with `pip install --help` shows a few ways, we will highlight the
two most common. The primary way is to use a "requirement specifier" for
packages on PyPI like `pip install <requirement specifier>` i.e. `pip install
numpy`. The other way, useful for local packages, takes your "local project path".
The "local project path" is the path to the root of your package, where the
`pyproject.yaml` file is located.

---
---

# Version Control: Git \& GitHub.com :octocat:

**Learning Goals: Tracking Changes and Collaborating**  :anchor:

- [ ] The "tracking changes" version control analogy 
- [ ] `git` setup on your computer
- [ ] `git` comfortable
- [ ] Grasp the distinction between `git` and GitHub.com
- [ ] Understand how to make a 'template' your own on GitHub.com

## Git Lesson 1: Version Control, a "Track Changes" Analogy :bowtie:

For those unfamiliar with version control tools, the workflow corresponds
well with common change-incorporation and draft-saving techniques from essay or
paper writing. You are most likely going to encounter--and solely use--a
tool called [git][ln_about_git] so we will address its high-level features
specifically.

**Drafting and Branching**

Saving "drafts," or keeping track of content milestones, is critical when
writing and coding. In essay writing, a "draft" marks a major development in content:
`my_sick_pape_FirstDraft.whatevs` might be the first pass, and
`my_sick_pape_ReworkedIntro.whatevs` modifies the first draft in hopes of a
stronger introduction. In `git` milestones are established by placing a tag on
all changes that fall within the same milestone. _Note: with code, the filename
is often important and should be static so that other code (and you) know where
to find a function. The 'milestone' tag is only visible to the user and git._ 
Since the changes leading to a milestone build on each other, one can
imagine coding towards a new milestone is akin to growing a new 'branch' off the
original 'tree.'  In fact, the milestones _are called_ "branches". One cool thing
about branches is that you can choose to keep them or not, and just like
saving drafts along the way you can easily visit these old milestones whenever
you like. If the branch works when you are done developing, there is a simple
procedure called 'merging' to fold it into the main code.

**Track Changes and Commits**

In common word processing software (Google Docks, Microsoft Word, and
LibreOffice) 'tracking changes' provides a non-destructive tool to record the
who, when, and why of each change. The word processor tracks every keystroke

and groups the changes by their spatial continuity in the document. In code,
changes are perhaps--in my view--best organized by functional impact. Binding
individual changes together is left up to the user. You must commit edited code
to the ledger of changes. Conveniently, we refer to 'tracked changes' in git as
"commits", and once a file has commits added to the ledger, or git log, git
refers to that file as "tracked."

**Seeing is Believing**

As I write this I'm growing a new branch (heading towards a milestone where the 
README.md is reorganized for our Mathematical Tools course, NBIO 228) and have just made a set
of individual changes constituting the section you just read. I'm arriving at a good
place to commit my changes to the log. After grasping how git works, this technical
output should read fairly naturally.  

<div align="center">
<img src="https://user-images.githubusercontent.com/26031420/157164148-c846d6c2-52bb-4a1e-a850-e0cf77d8ce61.png" 
width="80%"
title='
$ git status # ask git to tell me about my current position in editing space
On branch refactor_readme  # <-- this is the milestone im working towards so I gave the branch this name
Changes not staged for commit:  # <-- just reminding me that I need to commit them
    (use "git add <file>..." to update what will be committed) # <-----------.
    (use "git restore <file>..." to discard changes in working directory) # <-`-- git is super helpful and reminds the user
        modified:    README.md # <-- this "tracked" file has changes that can be committed to the change log
'
/>
</div>

## Git Lesson 2: Git Setup and First Steps :hugs:

### [Introducing yourself to git][ln_CNJCx_introgit] (<-- this won't teach you `git`, but it will make your life easier when you do)

Once you have `git` and a GitHub.com account, you are prepared to get this template repository
onto your personal machine. We will show you [git basics](#git-and-version-control-with-your-package) below.
For now lets get this repository on your machine so you can [skip to the learn python
part of the README.md](#an-introduction-to-python-nerd_face) if you want to get coding.

### Getting GitHub Repository On Your Machine

First, move to a location in your directory structure where you would like your git
repositories to live. 

```bash
mkdir ~/local_repos # make a new directory off of home (~)
cd $_ # '$_' is a little trick that holds the last input '~/local_repos' for you
```

Next, verify your directory position with `pwd`. Make sure you are where you want
to place \<your_new_repo\>. _Note, this command will not just dump the
contents into your current directory. A new folder will be made with the name
\<your_new_repo\> when you clone._

```bash
pwd # this command lets you know where you are in your directory structure
/path/to/local_repos
```

Finally, run the command below to `clone` the repository onto your machine. _To
copy the cloning link look for a green <kbd>code v</kbd> button towards the top
of every repo page._

```bash
git clone https://github.com/<user>/<your_new_repo>.git
```

Next, 'clone' the code from this repository onto your machine. You will need this code
to interact with the "learning python" material. The command below will automatically
place the code into the directory where you run the command from.

## Git Lesson 3: Git Comfortable :woman_technologist:

In this section you will learn the basic commands git commands. At a minimum you 
should `git clone` this repo so you have something to play with. _Probably best 
not to play around with code you care about, you might end up in a pinch if you
are exploring git for the first time_.

**Making a new branch**

Making a branch allows you to edit code while keeping your main branch
untouched.  This is powerful because you can always go back to the main branch
from the feature development branch. 

```
git checkout -b <branch_name>
```

**Making a commit**

This can be done on a new branch or while on the main branch. In a perfect world
you should make a commit every time you make a small describable change. 

**Moving between branches**

```
git branch # remind yourself of the branches available
  example_branch_of_interest
  main
* some_random_feature

git checkout example_branch_of_interest
```

**Merging a branch**

The merge command allows you to merge other branches onto the branch where 
you are currently sitting. Most commonly you will merge a branch that holds
a new feature into your main branch. 

```
git checkout main # go to the branch you'd like to merge into
git merge some_random_feature
```

**Learn more on your own**

With these [`git` basics and learning resources][ln_CNJCx_gitbasics] you should
be on your way in no time!

## Git Lesson 4: The `git` GitHub Relationship

GitHub is a place to store a `git` repository remotely. If you use `git ` and
GitHub by yourself GitHub acts like a specialized cloud backup. But GitHub is more than
just a storage area, it has a bunch of nice tools designed to help teams work on 
repositories together. Mainly these tools help manage merging branches and commits
from many contributors in parallel.

GitHub.com does a great job describing their role in this [Hello
World][ln_hw_github].


## Git Lesson 5: Using a Template

This template has "all" the components you need to make a python package of
your own (already setup for version control!). It is a skeleton that you can
use to establish _package_ structure for your project.

Getting started is as easy as hitting the ["Use this
template"](https://github.com/tgfisher/ouroboros/generate) button. Clone this
repository and clear out our code and replace it with yours: don't forget to
fill in the `pyproject.yaml` file with the content that matches your code structure.

---
---

### BONUS STUFF

```bash
printenv # we used an enviromental variable `PATH` above, run this to see 
           # _all_ your enviromental variables. Feel free to ask us if you 
           # want to understand what these are.
```
#### What Does 'Right' or 'Correct' Mean?

Ultimately, the 'right' or 'correct' way is the way that works well for
**you**. Doing something the 'right' way from the start of your life
as a pythonista will support a deeper understanding and establish habits that
promote better control over the code you write and the development
environments you create.

To me doing things the "right" way is a practice that will result in learning more,
coding clearer, working more efficiently, and preserving flexibility. If you see
a better way, get in touch via the github issues.

For example, _plotting the 'right' way_ allows you to manipulate
and alter your `figure`, and the `axes` that exist within it (e.g. 

```python
fig, ax = matplotlib.pyplot.subplots()
line = ax.plot(x_data, y_data)  # show linear interpolation between datapoints 
dots = ax.scatter(x_data, y_data, 'ro')  # indicator for each discrete point
```
).

Also, the 'right' command exposes you to useful parameters. Checking out the
[`matplotlib.pyplot.subplots` documentation][ln_matplotlibdoc] shows you how 
to control your plot from the start.

```python
fig,ax = matplotlib.pyplot.subplots(
    nrows=2,
    figsize=(10,3),
    dpi=150,
)  # higher resolution (dpi) with extra room (figsize) so dots can have own axes (nrows)
line = ax[0].plot(x_data, y_data)  # show linear interpolation between datapoints 
dots = ax[1].scatter(x_data, y_data, 'ro')  # indicator for each discrete point
```

Plotting the 'wrong' way obfuscates the fundamental elements, and requires more
calls to get what you need.
```python
lines = matplotlib.pyplot.plot(x_data, y_data)
fig = lines.get_figure()
ax = lines.axes
...
```

### Version control for jupyter notebooks

Yep, you should version control your notebooks. You might notice that 'tracking'
the changes in the .ipynb file is pretty tough--namely `git diff` isn't very readable
or helpful.

Jupyter notebooks don't play well with version control. The files aren't like
typical `.py` files. Each `.ipynb` file contains a lot of non-'human-friendly'
code. [Jupytext][ln_Jupytext_home] solves this, but takes a little getting used to.

#### Installing jupytext to your development workflow

Jupytext is a good candidate for your base python3 environment. Similar to `jupyter`,
it is nice to be able to run from the `jupytext` command without having to activate
your virtual environment. This being said, you are welcome to keep it within a
virtual environment.

```bash
python3 -m pip install jupytext # to put it into your base python3
source we_sick_venv/bin/activate
(we_sick_venv) $ pip install jupytext # to add to a specific venv
```

#### Tracking a notebook for the first time

_Note: tracking must be done on every new computer. The repo doesn't implicitly
know that you are using `jupytext`. If you clone onto a new machine you've got to
`pip install jupytext` and tell it to track._

This command is going to track your notebook, stored at <notebook_path>, as a
regular ipynb, a readable markdown (.md) file, and a runnable python (.py) file, wow!

```bash
jupytext --set-formats ipynb, py, md --sync <notebook_path>
```

[ln_interactivetutorial]:https://github.com/tgfisher/ouroboros/blob/main/notebooks/giocomo_python_interactive_reference.ipynb
[ln_CNJCx_terminalsetup]:https://github.com/stanford-cnjc/cnjcx-course-materials/blob/master/week1_commandline/cnjcx_week1_recap.md#bash-setup
[ln_CNJCx_commandlinetools]:https://github.com/stanford-cnjc/cnjcx-course-materials/blob/master/week1_commandline/cnjcx_week1_recap.md#finally-lets-get-git
[ln_CNJCx_introgit]: https://github.com/stanford-cnjc/cnjcx-course-materials/blob/master/week3_python/cnjcx_week3_recap.md#introducing-yourself-to-git
[ln_CNJCx_gitbasics]: https://github.com/stanford-cnjc/cnjcx-course-materials/blob/master/week4_codepractices/cnjcx_week4_resources.md
[ln_RealPython_packages]: https://realpython.com/python-modules-packages/
[ln_RealPython_home]: https://realpython.com/
[ln_CNJCx_home]: https://stanford-cnjc.github.io/#/CNJCx
[ln_Eshed_home]: https://eshedmargalit.com/
[ln_Homebrew_home]: https://brew.sh/
[ln_matplotlibdoc]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html
[ln_tucker_home]: https://tgfisher.github.io
[ln_linnie_twitter]: https://twitter.com/linniejiang
[ln_about_git]: https://git-scm.com/about
[ln_vscode_dl]: https://code.visualstudio.com/download
[ln_atom_dl]: https://atom.io/
[ln_sublime_dl]: https://www.sublimetext.com/
[ln_Jupytext_home]: https://github.com/mwouts/jupytext
[ln_zip_of_repo]: https://github.com/tgfisher/ouroboros/archive/refs/heads/main.zip 
[ln_python_colab]: https://colab.research.google.com/drive/1k4DY8BScPdxSYuqvYRX4qV27MFAtfKju?usp=sharing
[ln_about_modules]: https://docs.python.org/3/tutorial/modules.html
[ln_programmingmethods]: http://web.stanford.edu/class/cs106a/ 
[ln_learnpythonthehardway]: https://learncodethehardway.org/python/
[ln_hw_github]: https://docs.github.com/en/get-started/quickstart/hello-world
[ln_pypi]: https://pypi.org/
