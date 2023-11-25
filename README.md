# spot-gpt

Create an interaction between openAI gpt with a Boston SPOT robot

# Developing spot-gpt

## Prerequisites

- Make sure to have [python](https://www.python.org/downloads/) ver 3.7 or above installed in your desktop platform
  - *This project uses python ver 3.8.10. You can either install ver 3.8.10 or use pyenv*
- Install [pipenv](https://github.com/pypa/pipenv) for managing virtual environment and modules
- Install pyenv for managing python version if python is not ver 3.8.10
  - For UNIX/MacOS follow the installation process [here](https://github.com/pyenv/pyenv#installation)
  - For Windows follow the installation process [here](https://github.com/pyenv-win/pyenv-win)

## Cloning the repository

Clone the repository:

```
git clone https://github.com/SPOTGPT/spot-gpt
cd spot-gpt
```
Update to the latest commit by going to the spot-gpt working directory and run:
```
git pull
```

## Setup the environment
- If python 3.8.10 is not installed run:

  ```
  pyenv install 3.8.10
  ```
  to install python version 3.8.10

- On current working directory (where Pipfile is located) run:

  ```
  pipenv sync
  ```
  to install all needed packages, then run:
  ```
  pipenv shell
  ```
  to create the virtual environment.
- Make sure IDE is running the right interpreter created by pipenv shell.
- Create an environmental variable file called `.env` on `spot-gpt` working directory
  - write `OPENAI_API_KEY=***INSERT KEY HERE***` to that `.env` file.
  

