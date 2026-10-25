# Setup


**Setup Nvidia Build API and PydanticAI**

<a href="https://youtu.be/_wzRJde6r5M" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/ai_engineering/nvidia_build.png?raw=true" alt="" width="600">
</a>




## Github repo and uv

In the following we'll setup an empty github repository, clone it and then setup virtual environment using the package manager uv.

> [!NOTE]
> if you don't have uv installed do `pip install uv`


<!-- 
> [!NOTE]
> This is different from working with `uv venv`, `uv pip install ...`
> which are part of the manual workflow and is more traditional. Following the steps below with uv will show you modern and project approach to work with virtual environment. Also using `uv run` we won't need to activate virtual environment
>  -->

1. Create a github repository in github
2. Clone it to your desired path locally using git bash or terminal
3. Create a new uv project using

```bash
uv init --no-package --python 3.13
```

it will create the following for you

```
├── .gitignore
├── .python-version
├── README.md
├── main.py
├── pyproject.toml
└── uv.lock
```

4. Install neccessary packages

```bash
uv add pandas pydantic-ai ipykernel
```

We will install more packages when needing them

## Terminology


| glossary               | meaning                                                    |
| ---------------------- | ---------------------------------------------------------- |
| pyroject.toml          | metadata about your project                                |
| uv.lock                | info about projects dependencies - similar to requirements |
| .venv                  | virtual environment isolated from rest of system           |
| .python-version        | contains projects default python version                   |
| uv run <command>       | run command in project e.g. uv run python script.py        |
| uv init                | initialize python project - creates pyrpoject.toml         |
| uv add <package>       | add dependency to project and installs them                |
| uv add --dev <package> | add dev dependency                                         |
| uv remove <package>    | remove dependency from project                             |
| uv sync                | syncs the environment with pyproject.toml                  |
| uv python install      | install python version                                     |
| uv python list         | lists available python versions                            |
|                        |                                                            |

## Read more

- [uv on github](https://github.com/astral-sh/uv)

## Other videos 📹

- [python setup](https://www.youtube.com/watch?v=dteU94PSNoQ&t=90s)
- [python setup when it doesn't work](https://www.youtube.com/watch?v=Lkr6yRUCHbA&t=204s)
