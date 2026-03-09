<a name="top"></a>

# Cross Sum Number

<!-- image -->

<p align="center">
  <img src="assets/logo.png" alt="Cross Sum Number Icon" width="100">
</p>

A Cross Sum Number is a simple and engaging Python app where users calculate the sum of the digits in a given number. This project features a user-friendly graphical interface built with the `Tkinter` library, allowing users to easily input a number and instantly see the sum of its digits.

## Table of Contents

- [Technologies / Libraries Used](#technologies--libraries-used)
- [Getting Started](#getting-started)
- [Running Tests, Linting, and Formatting](#running-tests-linting-and-formatting)
- [Cross Sum Number Compiler](#cross-sum-number-compiler)
- [Continuous Integration (CI)](#continuous-integration-ci)
- [Contributing](#contributing)
- [License](#license)

## Technologies / Libraries Used

- [Python 3.14](https://www.python.org/) (current version used)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (for GUI)
- [PIP](https://pip.pypa.io/en/stable/) (Python package installer)
- [pytest](https://docs.pytest.org/en/stable/) (for testing)
- [pytest-mock](https://github.com/pytest-dev/pytest-mock) (for mocking in tests)

- [flake8](https://flake8.pycqa.org/en/latest/) (for code linting)
- [Black](https://black.readthedocs.io/en/stable/) (for auto-formatting)

## Getting Started

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

4. **Install/Upgrade Dependencies**:
   It's recommended to use a virtual environment for development. To set up and upgrade all dependencies (including pip), run:

   ```bash
   python -m pip install --upgrade pip
   pip install --upgrade -r dev-requirements.txt
   pip install black  # if not already present
   ```

   > ⚠️ **Note:** If you upgrade Python, always recreate your virtual environment and reinstall dependencies to avoid conflicts.

5. **Run the Application**:
   Launch the application by running the following command:

   ```bash
   python crossSum.py
   ```

## Running Tests, Linting, and Formatting

> **Note:** You can run tests and code quality checks either inside a virtual environment or globally, as long as all dependencies are installed. Using a virtual environment is recommended to avoid conflicts with system packages.

> **GUI Test Skipping:** Some GUI tests (those using Tkinter) may be skipped or error if your system's Tkinter/Tcl/Tk is not properly configured. This is expected on some Windows setups or minimal Python installations. The test suite is designed to skip these tests gracefully if the environment is not suitable, so you may see skipped or inconsistent results for GUI tests. All other tests will still run and report results normally.

To run the tests for the Cross Sum Number you can run the following commands in your terminal:

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

```bash
black app tests crossSum.py
```

This will automatically reformat your code to Black's style (default line length 88).

### Code Linting (flake8)

To check code quality with flake8:

```bash
flake8 .
```

**Notes:**

- The `.flake8` config ignores E501 (line too long) and uses a max line length of 88 to match Black's default. Let Black handle formatting.
- All tools (pytest, unittest, flake8, Black, etc.) work best in a virtual environment. Always activate your virtual environment before running tests or code quality checks.

### Recommended Workflow

1. **Format your code:**
   ```bash
   black app tests crossSum.py
   ```
2. **Lint your code:**
   ```bash
   flake8 .
   ```
3. **Run tests:**
   ```bash
   python -m pytest
   ```

## Cross Sum Number Compiler (Local Use Only)

You can compile the Cross Sum Number application into a standalone executable for your own local use using `PyInstaller`. This is useful if you want to run the app without Python installed. However, please note:

> **Warning:** The generated executable is intended for use on your own machine. Running the executable on remote or other machines may trigger antivirus false positives or fail due to environment differences. Distribution is not recommended.

To compile locally, follow these steps (**CMD** recommended on Windows):

1. **Set up your environment and dependencies** (see Getting Started above).
2. **Compile the application** (in your activated virtual environment):
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

## Continuous Integration (CI)

This project uses `GitHub Actions` for automated code quality and testing checks. Pipelines run on every push to the main branch and on every pull request.

For more information, check the GitHub Actions tab in your repository. If any issues are reported by the CI, review and fix them promptly to maintain code quality.

## Contributing

If you would like to contribute to the Cross Sum Number project, please follow these steps:

1. **Fork the Repository**: Click on the "Fork" button at the top right corner of the repository page.
2. **Create a New Branch**: Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b prefix/my-feature-branch
   ```
3. **Make Your Changes**: Make the necessary changes to the codebase.
4. **Commit Your Changes**: Commit your changes with a descriptive commit message:
   ```bash
   git commit -m "Add my feature"
   ```
5. **Push Your Changes**: Push your changes to your forked repository:
   ```bash
   git push origin my-feature-branch
   ```
6. **Create a Pull Request**: Go to the original repository and create a pull request from your forked repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

<p align="center">
   <a href="#top">Back to top</a>
</p>
