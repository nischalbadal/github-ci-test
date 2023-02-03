# Backend

## Setup

## Prerequisites

1. [Git](https://git-scm.com/downloads)
2. [Pyenv](https://github.com/pyenv/pyenv#getting-pyenv)

## Installation

- Clone the main repository locally.

  ```bash
  git clone git@github.com:laudio/vision.git
  ```
  
- Install [Python>=3.8](https://www.python.org/downloads/release/python-3816/).

  ```bash
  pyenv install 3.8.16
  ```

-  In `backend` directory

  ```
  pyenv local 3.8.16
  ```

- Install [Poetry](https://python-poetry.org/docs/).
- Use correct project environment using poetry.

  ```bash
  poetry env use 3.8.16
  ```

- Activate virtual environment.

  ```bash
  poetry shell
  ```

- Install dependencies using poetry.

  ```bash
  poetry install
  ```

  > Use command like : `poetry show --tree` to get information about installed dependencies.

## Run locally

```bash
flask --app src/__main__.py run
```

## Test

```bash
chmod +x test.sh
./test.sh
```

## Migrations

[Alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html) is used for migration environment.

Create migration files.

```bash
alembic revision -m "create users example"
```

This creates migration file with name `revision_create_users.py` in `alembic/versions/` folder. Edit queries in `upgrade()` and `downgrade()` functions accordingly.

Running migrations.

```bash
alembic upgrade head
```

Rolling back migrations.

```bash
alembic downgrade -1
```

## License

[LICENSE](./LICENSE.md) : (c) [Laudio, Inc.](https://laudio.com/) All Rights Reserved.
