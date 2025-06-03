import os
from app.gui import Window

# MAIN file for the Cross Sum Number project.
def run_app():
    """
    Run the GUI application for the Cross Sum Number project.
    When the windows is closed, will execute the automatic tests.
    """
    app = Window()
    app.__main__()  # Initialize the GUI application
    app.run()  # Start the main loop of the application


if __name__ == "__main__":
    if os.getenv("RUNNING_TESTS") != "1":  # only run the app if not running tests
        run_app()
