import subprocess
import sys
import os


def run_tests():
    """
    Run the tests for the Cross Sum Number project.
    """
    print("\n[Info] Running tests with unittest...")
    unittest_result = subprocess.call(
        [
            sys.executable,
            "-m",
            "unittest",
            "discover",
            "-s",
            "tests",
            "-p",
            "test_*.py",
        ],
        env={**os.environ, "RUNNING_TESTS": "1"},  # Set environment variable to indicate tests are running
    )

    print("\n[Info] Running tests with pytest...")
    pytest_result = subprocess.call(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/test_gui.py",
            "-v",
        ],
        env={**os.environ, "RUNNING_TESTS": "1"},
    )

    if unittest_result == 0 and pytest_result == 0:
        print("\n[Info] ✅ All tests passed successfully!")
    else:
        print("\n[Error] ❌ Some tests failed. Please check the output above.")
        sys.exit(1)


if __name__ == "__main__":
    run_tests()
