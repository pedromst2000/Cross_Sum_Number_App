<a name="top"></a>

# Cross Sum Number

<!-- image -->

<p align="center">
  <img src="assets/logo.png" alt="Cross Sum Number Icon" width="100">
</p>

A Cross Sum Number is a simple and engaging Python app where users calculate the sum of the digits in a given number. This project features a user-friendly graphical interface built with the `Tkinter` library, allowing users to easily input a number and instantly see the sum of its digits.

## 📑 Table of Contents

- [📚 Technologies / Libraries Used](#-technologies--libraries-used)
- [🚀 Getting Started](#-getting-started)
- [🧪 Running Tests, Linting, and Formatting](#-running-tests-linting-and-formatting)
- [🛠️ Cross Sum Number Compiler](#️-cross-sum-number-compiler)
- [🔄 Continuous Integration (CI)](#-continuous-integration-ci)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## 📚 Technologies / Libraries Used

- [Python 3.14](https://www.python.org/) (current version used)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (for GUI)
- [PIP](https://pip.pypa.io/en/stable/) (Python package installer)
- [pytest](https://docs.pytest.org/en/stable/) (for testing)
- [pytest-mock](https://github.com/pytest-dev/pytest-mock) (for mocking in tests)

- [flake8](https://flake8.pycqa.org/en/latest/) (for code linting)
- [yamllint](https://yamllint.readthedocs.io/en/stable/) (for YAML linting)
- [Black](https://black.readthedocs.io/en/stable/) (for auto-formatting)

## 🚀 Getting Started

### ⚙️ Prerequisites

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

   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\Activate
   # On macOS/Linux:
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

## 🧪 Running Tests, Linting, and Formatting

> **Note:** Use a virtual environment for best results.

To run all tests:

```bash
python -m pytest
```

or

```bash
python run_tests.py
```

or for unittest framework:

- On **Windows**:
  ```bash
  python -m unittest discover -s tests
  ```
- On **macOS/Linux**:
  ```bash
  python3 -m unittest discover -s tests
  ```

### Code Formatting (Black)

To auto-format your codebase using [Black](https://black.readthedocs.io/en/stable/):

First, install Black in your (virtual) environment if it is not already installed:

```bash
pip install black
```

Then run:

```bash
black app tests crossSum.py
```

### Code Linting (flake8 & yamllint)

To check code quality with flake8:

```bash
flake8 .
```

To lint YAML files with yamllint:

```bash
yamllint .
```

> **Note:** All YAML files must use LF (Unix) line endings. This is enforced by the `.gitattributes` file in the repository. If you see yamllint errors about line endings, convert the file to LF in your editor before committing.

<!-- To auto-format YAML files with yamlfmt:

```bash
yamlfmt -w .
``` -->

**If not using a virtual environment:**

- Use `python -m black ...`, `python -m flake8 ...`, and `python -m yamllint ...` instead of the short commands, e.g.:
  ```bash
  python -m black app tests crossSum.py
  python -m flake8 .
  python -m yamllint .
  ```
- In a virtual environment, you can use `black`, `flake8`, and `yamllint` directly after activation.

**Notes:**

- The `.flake8` config ignores E501 (line too long) and uses a max line length of 88 to match Black's default.
- The `.yamllint.yaml` config is used for YAML linting rules.
- All tools work best in a virtual environment, where you can use the short commands (`black`, `flake8`, `yamllint`) directly after activation.

### Recommended Workflow

> **Note:** Always run the formatting, linting, and test commands below before committing your code. This helps prevent CI pipeline failures. If your CI fails, check the GitHub Actions tab for issues and fix them promptly.

1. **Format your code:**
   ```bash
   black app tests crossSum.py
   ```
2. **Lint your code:**
   ```bash
   flake8 .
   ```
3. **Lint YAML files:**

   ```bash
   yamllint .
   ```

4. **Run tests:**
   ```bash
   python -m pytest
   ```

# 🛠️ Cross Sum Number Compiler

You can compile the Cross Sum Number application into a standalone executable for your own local use using `PyInstaller`. This is useful if you want to run the app without Python installed. However, please note:

> **Warning:** The generated executable is intended for use on your own machine. Running the executable on remote or other machines may trigger antivirus false positives or fail due to environment differences. Distribution is not recommended.

To compile locally, follow these steps:

1. **Set up your environment and dependencies** (see Getting Started above).
2. **Activate your virtual environment** (see instructions above).
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
     > ⚠️ **Note:** The standalone executable will be in the `dist` folder as `crossSum.exe`. Use it locally on your own machine.

## 🔄 Continuous Integration (CI)

This project uses `GitHub Actions` for automated code quality and testing checks. Pipelines run on every push to the main branch and on every pull request.

For more information, check the GitHub Actions tab in your repository. If any issues are reported by the CI, review and fix them promptly to maintain code quality.

## 🤝 Contributing

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

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

<p align="center">
   <a href="#top">Back to top</a>
</p>
