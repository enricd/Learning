# pytest Master Class

[Link to the YouTube video - pytest master class by Noah Gift](https://www.youtube.com/watch?v=IN4qt-9bMiE&ab_channel=PragmaticAILabs)

# 1. Intro
## 1.1. DevOps:
CI/CD, from Dev to Test to Prod  
CI: Code Works?

# 2. Setting up environment

(Possible to use GitHub Codespaces)

### venv

```console
$ python -m venv ~/.venv  
or  
$ virtualenv ~/.venv
```

### Activating the venv automatically when opening a new terminal:

```console
$ vim ~/.bashrc
```

Shift + G  (go to the bottom of the file)  
Add to the bottom of the file:  

```console
# Source VirualENV
source ~/.venv/bin/activate
```

:wq  (write and exit)  

## 2.1. Project Scaffolding

```console
$ touch Makefile
$ touch requirements.txt
$ touch hello.py
$ touch test_hello.py
```

Complete Makefile, requirements and more_hello() func in hello.py, then:

```console
$ make install
```

```console
$ ipython
```

```ipython
from hello import more_hello

more_hello()
>>> "hi"

assert more_hello() == "hi"

exit()
```

Pass this logic to the test_hello.py file, then:

```console
$ make test
```

Linting will catch nonesense code and errors, we are disabling R (Refactor) and C (Convention)

```console
$ make lint
```

The format tool will clean the code and make it uniform in terms of style

```console
$ make format
```

Then let's add versions to requirements.txt packages

```console
$ make pip freeze | less
```

Manually copy and paste the "==" sign and the version for each of the preexisten packages in the list  

Finally:

```console
$ make all
```

And git add, commit and push the repo to GitHub 


# 3. Build System
Allows to build specific images and configurations for each environment, after developing and testing locally.  

Use GitHub Actions to CI new changes in a repo.  
Create a ./.github/workflows folder and then a testing-ci.yml file with the proper build steps.  

It is possible to add an status badge to the main Readme.md file of the repo to automatically see the status of every CI pipeline last build.  


# 4. AWS Cloud9

Previous test:  
Open a AWS CloudShell from the AWS account, clone the github project and setup a venv.  
Then "$ Make all" (you can do vim Makefile to read it first).

AWS Cloud9 is a cloud-based IDE that lets you write, run, and debug your code with just a browser. Launch a new Cloud9 environment from your AWS account, selecting requiered hw specs and OS. It is similar to GitHub Codespaces but to work in the AWS environment.  
To start working in the Cloud9 new env, just repeat steps done previously in CloudShell.


# 5. AWS CodeBuild

Search CodeBuild in your AWS account.   
Create build project.  
Project name and Description. Enable build badge.  
Source: provide the source of the code.  
Webhooks options to trigger builds.  
Environment options: chose the same or a similar env where the code has to run.ç
Buildspec options: provide build commands directly on the provided editor or in a buildspec.yml file in the project.  
Batch, Artifacts and Logs options.  

Start build. Check logs at Tail Logs.  
Copy the badge URL to the Readme file.


# 6. nbval to test py notebooks

Add a .ipynb file to the project with test assert cells in it.  
Install nbval py package and add pytest line in the Makefile for nbval on the .ipynb file.  


# 7. pytest Fixtures

Fixtures are decorators to declare functions that arrange previous steps for testing


# 8. Flask


# 9. Pytest with Click command-line testing


