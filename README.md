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
- [🛠️ Cross Sum Number Compiler](#-cross-sum-number-compiler-local-use-only)
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

To get started with the Cross Sum Number project, follow these steps:

1. **Clone the Repository**:
   Open your terminal (preferably using **Git Bash**) and execute the following command to clone the repository:

   ```bash
   git clone https://github.com/pedromst2000/Cross_Sum_Number_App.git
   ```

   > ⚠️ **Note:** Ensure you have `git` installed. Download it from the [official Git website](https://git-scm.com/downloads) if needed. To open **Git Bash** on your Desktop, right-click and select `Open Git Bash here` (you may need to click `Show more options` to find this entry).

2. **Navigate to the Project Directory**:

   ```bash
   cd Cross_Sum_Number_App
   ```

3. **Check Python Version**:
   Ensure you are using Python 3.14 (or newer). You can check your Python version by running:

   ```bash
   python --version
   ```

   > ⚠️ **Note:** You may need to install Python 3.14 if it is not already installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

   If you have both Python 2 and Python 3 installed, you may need to use `python3` instead of `python`.

4. **Set Up and Activate a Virtual Environment (Recommended):**
   Using a virtual environment is recommended to isolate dependencies and avoid conflicts.
   - To create a virtual environment:

     ```bash
     python -m venv .venv
     ```

     > ⚠️ **Note:** This command creates a new virtual environment named `.venv` in your project folder. Run it once unless you want to recreate the environment.

   - To activate the virtual environment:
     - On **Windows (CMD or PowerShell):**
       ```bash
       .venv\Scripts\Activate
       ```
     - On **macOS/Linux (Bash):**
       ```bash
       source .venv/bin/activate
       ```

   - Once activated, upgrade pip and install dependencies:

     ```bash
     python -m pip install --upgrade pip
     pip install --upgrade -r dev-requirements.txt
     ```

     > ⚠️ **Note:** If you upgrade Python, always recreate your virtual environment and reinstall dependencies to avoid conflicts.

   - To deactivate the virtual environment and switch back to your default (system) Python:
     ```bash
     deactivate
     ```
     > ⚠️ **Note:** After deactivating, any Python commands will use your system Python and its packages.

5. **Run the Application**:
   Launch the application by running the following command:

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

## 🛠️ Cross Sum Number Compiler

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
