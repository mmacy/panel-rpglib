# Contributing to Arbrynnica

Thank you for your interest in contributing to Arbrynnica! This document provides instructions for setting up the development environment and contributing to the project.

## Development process

We follow an iterative development process with a strong emphasis on unit tests to maintain high code quality. Continuous integration and automated testing are integral to our workflow, ensuring a stable and reliable codebase.

## Development environment setup

### Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.11](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Rye](https://rye.astral.sh)

### Set up the repository

1. **Clone the repository**:

   ```sh
   git clone <repository-url>
   cd arbrynnica
   ```

2. **Install Rye** (if not already installed):

   Follow the instructions on the [Rye website](https://rye.astral.sh).

3. **Initialize the project with Rye**:

   ```sh
   rye init arbrynnica
   ```

4. **Add project dependencies**:

   ```sh
   rye add pytest mypy ruff isort
   ```

5. **Create and activate a virtual environment** (handled by Rye):

   ```sh
   rye sync
   ```

### Configure Visual Studio Code

1. **Install the following VS Code extensions**:
   - Python by Microsoft
   - Pylance
   - Ruff Formatter
   - isort

2. **Open the project in VS Code**:

   ```sh
   code .
   ```

3. **Configure VS Code settings**:

   - Ensure your workspace settings (`.vscode/settings.json`) include the following configurations:

   ```json
   {
     "python.pythonPath": ".venv/bin/python", // Adjust if necessary
     "python.formatting.provider": "none",
     "editor.formatOnSave": true,
     "[python]": {
       "editor.defaultFormatter": "charliermarsh.ruff"
     },
     "editor.codeActionsOnSave": {
       "source.organizeImports": true
     },
     "python.linting.mypyEnabled": true,
     "python.linting.enabled": true,
     "editor.rulers": [120]
   }
   ```

### Run tests

1. **Run tests using pytest**:

   ```sh
   rye run pytest
   ```

2. **Check types with mypy**:

   ```sh
   rye run mypy src tests
   ```

3. **Lint and format code with ruff and isort**:

   ```sh
   rye run ruff check src tests
   rye run isort .
   ```

4. **Ensure all tests pass** before committing and pushing your changes.

### Contribute code

1. **Create a new branch** for your feature or bugfix:

   ```sh
   git checkout -b feature/description
   ```

2. **Make your changes**. Ensure that your code adheres to the project's coding standards and passes all tests.

3. **Commit your changes**:

   ```sh
   git add .
   git commit -m "Description of the changes"
   ```

4. **Push your branch** to GitHub:

   ```sh
   git push origin feature/description
   ```

5. **Create a pull request** on GitHub. Provide a clear description of your changes and ensure all checks pass.

### Additional guidelines

- **Code style**: Follow the Google Python Style Guide, with a line length limit of 120 characters.
- **Documentation**: Update documentation to reflect your changes, including docstrings and README.md if necessary.
- **Reviews**: Address any feedback during the code review process promptly.

By following these instructions, you'll help maintain a clean, efficient, and collaborative development environment. Thank you for contributing to Arbrynnica!
