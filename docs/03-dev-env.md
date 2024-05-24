# Arbrynnica development environment spec

## Source control

**Git and GitHub**

- Use Git for version control.
- Host the repository on GitHub for issue tracking and collaboration.
- Set up branch protection rules and use pull requests for code reviews.

## IDE

**Visual Studio Code**

- Install VS Code and the following extensions:
  - Python by Microsoft
  - Pylance
  - Ruff Formatter
  - isort

## Python environment and package management

**Rye**

- Install Rye:

  ```sh
  pip install rye
  ```

- Create a new project and `pyproject.toml`:

  ```sh
  rye init arbrynnica
  ```

- Add dependencies:

  ```sh
  rye add pytest mypy ruff isort
  ```

## Testing framework

**pytest**

- Create a `tests` directory with initial test files.
- Configure pytest in `pyproject.toml`:

  ```toml
  [tool.pytest.ini_options]
  addopts = "--strict-markers"
  testpaths = ["tests"]
  ```

## Static type checking and code formatting

**mypy**

- Configure mypy in `pyproject.toml`:

  ```toml
  [tool.mypy]
  strict = true
  ```

**ruff and isort**

- Configure ruff and isort in `pyproject.toml`:

  ```toml
  [tool.ruff]
  line-length = 120

  [tool.isort]
  profile = "black"
  ```

## Serialization

**json**

- Use JSON for saving and loading game states.
