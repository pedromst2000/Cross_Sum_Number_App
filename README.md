<a name="top"></a>

<!-- image -->

<p align="center">
  <img src="assets/logo.png" alt="Cross Sum Number Icon" width="100">
</p>

<h1 align="center">Cross Sum Number</h1>

<p align="center">
   <a href="https://github.com/pedromst2000/Cross_Sum_Number_App/actions/workflows/test.yml">
      <img src="https://github.com/pedromst2000/Cross_Sum_Number_App/actions/workflows/test.yml/badge.svg" alt="Tests" />
   </a>
   <a href="https://github.com/pedromst2000/Cross_Sum_Number_App/actions/workflows/lint.yml">
      <img src="https://github.com/pedromst2000/Cross_Sum_Number_App/actions/workflows/lint.yml/badge.svg" alt="Lint Code Quality" />
   </a>
   <a href="https://codecov.io/gh/pedromst2000/Cross_Sum_Number_App">
      <img src="https://codecov.io/gh/pedromst2000/Cross_Sum_Number_App/graph/badge.svg" alt="Coverage" />
   </a>
</p>
A Cross Sum Number is a simple and engaging Python app where users calculate the sum of the digits in a given number. This project features a user-friendly graphical interface built with the `Tkinter` library, allowing users to easily input a number and instantly see the sum of its digits.

## :bookmark_tabs: Table of Contents

- [:books: Technologies / Libraries Used](#books-technologies--libraries-used)
- [:clapper: Demo Video](#clapper-demo-video)
- [:rocket: Getting Started](#rocket-getting-started)
  - [:gear: Prerequisites](#gear-prerequisites)
- [:test_tube: Running Tests, Linting, and Formatting](#test_tube-running-tests-linting-and-formatting)
- [:hammer_and_wrench: Standalone Executable](#hammer_and_wrench-standalone-executable)
- [:arrows_counterclockwise: Continuous Integration (CI)](#arrows_counterclockwise-continuous-integration-ci)
- [:handshake: Contributing](#handshake-contributing)
- [:page_facing_up: License](#page_facing_up-license)

# :books: Technologies / Libraries Used

**Core Technologies**

- [Python 3.14+](https://www.python.org/) — Main programming language.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — GUI framework.
- [pip](https://pip.pypa.io/en/stable/) — Package manager.

**Testing**

- [pytest](https://docs.pytest.org/en/stable/) — Testing framework.
- [pytest-mock](https://github.com/pytest-dev/pytest-mock) — Mocking in tests.
- [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) — Test coverage reporting.

**Code Quality & Linting**

- [Black](https://black.readthedocs.io/en/stable/) — Code formatter.
- [flake8](https://flake8.pycqa.org/en/latest/) — Code linter.
- [yamllint](https://yamllint.readthedocs.io/en/stable/) — YAML file linting.

**Packaging**

- [PyInstaller](https://www.pyinstaller.org/) — Build standalone executables.

# :clapper: Demo Video

[![Demo Video](https://img.youtube.com/vi/I1cHkolX1NI/0.jpg)](https://youtu.be/I1cHkolX1NI)

<p align="center">
  <a href="https://youtu.be/I1cHkolX1NI" target="_blank">
    <img src="https://img.shields.io/badge/Watch%20on-YouTube-red?logo=youtube&logoColor=white&style=for-the-badge" alt="Watch on YouTube" />
  </a>
</p>

---

# :rocket: Getting Started

### :gear: Prerequisites

- **Python 3.14+** installed ([download](https://www.python.org/downloads/))
- **pip** (comes with Python)
- **git** (for cloning, [download](https://git-scm.com/downloads))
- (Recommended) **Virtual environment** support: `python -m venv`
- (Optional) **PyInstaller** for building executables

> Make sure Python and pip are available in your system PATH. You can check with:
>
> ```bash
> python --version
> pip --version
> ```

To get started:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pedromst2000/Cross_Sum_Number_App.git
   cd Cross_Sum_Number_App
   ```
2. **(Recommended) Create and activate a virtual environment:**

   Create the virtual environment:

   ```bash
   python -m venv .venv
   ```

   Activate it on **Windows**:

   ```bash
   .venv\Scripts\Activate
   ```

   Activate it on **macOS/Linux**:

   ```bash
   source .venv/bin/activate
   ```

   > **To deactivate the virtual environment:**
   >
   > - On any OS, simply run:
   >   ```bash
   >   deactivate
   >   ```
   >   This will return you to your system's default Python environment.

   > **Note:** Some dependencies may only work correctly inside the `.venv` virtual environment. It is highly recommended to use the virtual environment for all development and testing.

3. **Install dependencies:**

   ```bash
   python -m pip install --upgrade pip
   pip install --upgrade -r dev-requirements.txt
   ```

   > **Troubleshooting:**
   > If you see `ModuleNotFoundError` or similar errors when running the app or tests, it usually means the required dependencies are not installed in your current Python environment.
   >
   > - If you are **not** using the `.venv` virtual environment, you must install the dependencies in your active environment as well:
   >   ```bash
   >   pip install --upgrade -r dev-requirements.txt
   >   ```
   > - For best results, always activate the `.venv` before installing or running anything.

4. **Run the app:**
   ```bash
   python crossSum.py
   ```

# :test_tube: Running Tests, Linting, and Formatting

> **Tip:** Use a virtual environment for best results.

## Testing

This project uses [pytest](https://docs.pytest.org/en/stable/) for all tests (unit, integration, and UI). Tests are located in the `tests/` directory and follow the naming convention `test_*.py`.

To run all tests, use one of the following commands:

**Option 1: Using pytest directly**

```bash
python -m pytest
```

**Option 2: Using the test runner script**

```bash
python run_tests.py
```

### Test Coverage

> **Note:** `pytest-cov` is included in `dev-requirements.txt`. Verify installation with:
>
> ```bash
> python -m pip show pytest-cov
> ```

Run tests with coverage reporting:

```bash
python -m pytest --cov=app --cov-report=term-missing
```

Generate XML for CI/tools:

```bash
python -m pytest --cov=app --cov-report=xml
```

**Troubleshooting:**

- If you see `ModuleNotFoundError: No module named 'app'`, set `PYTHONPATH`:
  - On Windows (PowerShell):

  ```powershell
  $env:PYTHONPATH = "$PWD"
  ```

  - On Linux/macOS:

  ```bash
  export PYTHONPATH=$PWD
  ```

  Then re-run pytest.

- If pytest is not found and you haven't activated the venv, use `python -m pytest` (shown above) — this works regardless of PATH.

## Formatting & Linting

Run these commands to format and lint your code:

```bash
python -m black app tests crossSum.py  # Format code
```

```bash
python -m flake8 .  # Lint Python
```

```bash
python -m yamllint .  # Lint YAML
```

> **Note:** All YAML files must use LF (Unix) line endings. If you see yamllint errors about line endings, convert the file to LF in your editor before committing.

## Recommended Workflow

Before committing code, run this checklist:

1. Format code with Black

   ```bash
   python -m black app tests crossSum.py
   ```

2. Lint Python code with flake8

   ```bash
   python -m flake8 .
   ```

3. Lint YAML files with yamllint

   ```bash
   python -m yamllint .
   ```

4. Run all tests
   ```bash
   python -m pytest
   ```

> This helps prevent CI failures. If CI fails, check the GitHub Actions tab for details and fix issues promptly.

# :hammer_and_wrench: Standalone Executable

You can compile the Cross Sum Number application into a self-contained application folder using `PyInstaller`, which bundles everything needed to run it — no Python installation required. However, please note:

> **Warning:** The generated executable is intended for use on your own machine. Running the executable on remote or other machines may trigger antivirus false positives or fail due to environment differences. Distribution is not recommended.

To compile locally, follow these steps:

1. **Set up your environment and dependencies** (see [Getting Started](#rocket-getting-started) above).
2. **Activate your virtual environment** (see [Getting Started](#rocket-getting-started) above).
3. **Install PyInstaller in your virtual environment**:
   ```bash
   pip install pyinstaller
   ```
4. **Compile the application** (in your activated virtual environment):
   - **On Windows (CMD or PowerShell), run as a single line:**

     ```cmd
     pyinstaller crossSum.py --noconsole --add-data "app/assets/icon/Icon.ico;app/assets/icon" --distpath dist --workpath build --specpath . --name crossSum
     ```

     > _Advanced:_ In PowerShell, you can use the backtick (`) for line continuation. In CMD, use the caret (^) for line continuation.

   - **On Linux/macOS (bash/zsh), you can use line continuations:**
     ```bash
     pyinstaller crossSum.py \
        --noconsole \
        --add-data "app/assets/icon/Icon.ico;app/assets/icon" \
        --distpath dist \
        --workpath build \
        --specpath . \
        --name crossSum
     ```

   > ⚠️ **Note:**
   >
   > After running PyInstaller, a `dist/` folder will be created.
   >
   > Inside `dist/`, you will find a folder named `CrossSum`.
   >
   > This `CrossSum` folder contains a standalone, portable application. You can move this folder anywhere on your own system (e.g., Desktop) and run `CrossSum.exe` directly—**you do not need to have Python installed to run the executable**. All necessary Python components are bundled inside.
   >
   > **However, you do need Python installed to build (compile) the executable with PyInstaller.**
   >
   > ⚠️ Do not remove the `_internal` folder, as it is required for the application to function properly.

# :arrows_counterclockwise: Continuous Integration (CI)

This project uses `GitHub Actions` for automated code quality and testing checks. Pipelines run on every push to the main branch and on every pull request.

For more information, check the GitHub Actions tab. If any issues are reported by the CI, review and fix them promptly to maintain code quality.

# :handshake: Contributing

**How to contribute:**

1. **Fork** this repo and clone your fork
2. **Create a branch:**
   ```bash
   git checkout -b <type>/<short-description>
   ```
3. **Make your changes**
4. **Commit:**
   ```bash
   git commit -m "<type>: <short description>"
   ```
5. **Push:**
   ```bash
   git push origin <type>/<short-description>
   ```
6. **Open a Pull Request**

**Commit/branch types:**

- feat: new feature
- fix: bug fix
- docs: documentation
- style: formatting
- chore: maintenance
- ci: CI pipelines

**PR checklist:**

- Follows naming conventions
- Describes changes clearly
- Passes all CI checks (formatting, linting, tests)
- No merge conflicts

Thanks for contributing! 🎉

# :page_facing_up: License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

<p align="center">
   <a href="#top">Back to top</a>
</p>
