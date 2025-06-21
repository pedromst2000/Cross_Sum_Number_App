# Cross Sum Number

A Cross Sum Number is a simple and engaging Python project where users calculate the sum of the digits in a given number. This project features a user-friendly graphical interface built with the `Tkinter` library, allowing users to easily input a number and instantly see the sum of its digits.

## Table of Contents

- [Technologies / Libraries Used](#hammer_and_wrench-technologies--libraries-used)
- [Getting Started](#rocket-getting-started)
- [Running Tests](#test_tube-running-tests)
- [Compiler](#computer-cross-sum-number-compiler)
- [Download Executable](#link-download-executable)
- [Contributing](#handshake-contributing)
- [License](#page_facing_up-license)
- [Contact](#email-contact)

## :hammer_and_wrench: Technologies / Libraries Used

- [Python 3.x](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (for GUI)
- [PIP](https://pip.pypa.io/en/stable/) (Python package installer)
- [pytest](https://docs.pytest.org/en/stable/) (for testing)
- [pytest-mock](https://github.com/pytest-dev/pytest-mock) (for mocking in tests)

## :rocket: Getting Started

To get started with the Cross Sum Number project, follow these steps:

1. **Clone the Repository**:
   Open your terminal and run the following command to clone the repository:

   ```bash
   git clone https://github.com/pedromst2000/Cross_Sum_Number_App.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd Cross_Sum_Number_App
   ```

3. **Check Python Version**:
   Ensure you are using Python 3.x. You can check your Python version by running:

   ```bash
   python --version
   ```

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

To compile the Cross Sum Number application into an executable, you can use `PyInstaller`. Follow these steps:

1. **Install PyInstaller**:
   If you haven't already installed PyInstaller, you can do so using pip:

   ```bash
   pip install pyinstaller
   ```

2. **Compile the Application**:
   You can compile the application by running the following command:

   ```bash
   pyinstaller crossSum.py --name crossSum --windowed --onefile --noupx 
   --icon=assets/icon/icon.ico --add-data "assets/icon/icon.ico;assets/icon"
   ```
   This command will create a standalone executable in the `dist` directory. From there, you can run the application without needing to have Python installed on the target machine.


##  :link: Download Executable

In the following link you can download the Cross Sum Number executable:

https://github.com/pedromst2000/Cross_Sum_Number_App/releases/tag/v1.0.0

Within the release's **`Assets`** section, you will find a **`ZIP`** file **`crosssum-windows.zip`**
 containing the standalone executable. Simply download and extract it to run the application on your machine—no need to install Python or any additional dependencies.

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
