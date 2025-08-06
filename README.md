# Cross Sum Number


![Cross Sum Number](assets/icon/icon.ico)

A Cross Sum Number is a simple and engaging Python app where users calculate the sum of the digits in a given number. This project features a user-friendly graphical interface built with the `Tkinter` library, allowing users to easily input a number and instantly see the sum of its digits.

## Table of Contents

- [Technologies / Libraries Used](#hammer_and_wrench-technologies--libraries-used)
- [Getting Started](#rocket-getting-started)
- [Running Tests](#test_tube-running-tests)
- [Compiler](#computer-cross-sum-number-compiler)
- [Contributing](#handshake-contributing)
- [License](#page_facing_up-license)
- [Contact](#email-contact)

## :hammer_and_wrench: Technologies / Libraries Used

- [Python 3.x](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (for GUI)
- [PIP](https://pip.pypa.io/en/stable/) (Python package installer)
- [pytest](https://docs.pytest.org/en/stable/) (for testing)
- [pytest-mock](https://github.com/pytest-dev/pytest-mock) (for mocking in tests)
- [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/) (for compiling the application into an executable)

## :rocket: Getting Started

To get started with the Cross Sum Number project, follow these steps:

1. **Clone the Repository**:
   Open your terminal (preferably using **Git Bash**) and execute the following command to clone the repository:

   ```bash
   git clone https://github.com/pedromst2000/Cross_Sum_Number_App.git
   ```

   > ⚠️ **Note:** Make sure you have `git` installed on your machine. If you don't have it, you can download it from the [official Git website](https://git-scm.com/downloads).

2. **Navigate to the Project Directory**:

   ```bash
   cd Cross_Sum_Number_App
   ```

3. **Check Python Version**:
   Ensure you are using Python 3.x. You can check your Python version by running:

   ```bash
   python --version
   ```

   > ⚠️ **Note:** You may need to install Python 3.x if it is not already installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

   If you have both Python 2 and Python 3 installed, you may need to use `python3` instead of `python`.

4. **Upgrade pip**:
   It's a good practice to ensure that `pip` is up to date. You can upgrade it by running:

   ```bash
   python -m pip install --upgrade pip
   ```

5. **Install Required Libraries**:
   Ensure you have Python installed on your machine. You can install the required libraries for this project using pip:

   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Application**:
   Launch the application by running the following command:

   ```bash
   python crossSum.py
   ```

## :test_tube: Running Tests

To run the tests for the Cross Sum Number you can run the following commands in your terminal:

```bash
python -m pytest
```

or

```bash
python run_tests.py
```

or for unittest framework:

```bash
python3 -m unittest discover -s tests
```

## :computer: Cross Sum Number Compiler

To compile the Cross Sum Number application into a standalone executable, use `PyInstaller` by following these steps in your terminal (**CMD**):

Run the terminal (**CMD**) inside the repository.

1. **Create virtual environment** (optional but recommended):
   Creating a virtual environment is optional but highly recommended. It helps isolate your project's dependencies, preventing conflicts with other Python packages and ensuring a smoother compilation process. To set up a virtual environment with `Python 3.11`, run:

   ```bash
   py -3.11 -m venv venv
   ```

   > ⚠️ **Note:** For best results, use Python 3.11 in a virtual environment when compiling. PyInstaller 5.10.1 is required for compatibility; newer versions may not work properly with Python 3.11 and can change the build structure (e.g., adding an `_internal` folder), which complicates the final `dist/` output and may lead to issues with the executable.

2. **Activate the virtual environment**:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

     > ⚠️ **Note:** To deactivate the virtual environment, simply run `deactivate` in your terminal.

3. **Install dependencies**:
   Make sure you have the required dependencies installed in your virtual environment. You can install them using:

   ```bash
   pip install -r dev-requirements.txt
   ```

   > ⚠️ **Note:** Before proceeding, ensure that you have the correct version of `PyInstaller` installed and `python` in the virtual environment.

4. **Compile the application**:
   Run the following command in your activated virtual environment to compile the application:

   ```bash
   pyinstaller crossSum.py ^
      --noconsole ^
      --add-data "assets/icon/icon.ico;assets/icon" ^
      --distpath dist ^
      --workpath build ^
      --specpath . ^
      --name crossSum
   ```

   > ⚠️ **Note:** After running the above command, the standalone executable will be located in the `dist` folder. To launch the application, run `crossSum.exe` from that directory.

## :handshake: Contributing

If you would like to contribute to the Cross Sum Number project, please follow these steps:

1. **Fork the Repository**: Click on the "Fork" button at the top right corner of the repository page.
2. **Create a New Branch**: Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b my-feature-branch
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

## :page_facing_up: License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## :email: Contact

For any questions or suggestions, feel free to contact me at:

Email: [pedromst2000@gmail.com](mailto:pedromst2000@gmail.com)

LinkedIn: [Pedro Teixeira](https://www.linkedin.com/in/pedromst2000)

<p align="center">
 <a href="#top">Back to top</a>
</p>
