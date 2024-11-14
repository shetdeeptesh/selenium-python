# run.py

import argparse
import sys
import importlib.util
import os
from tabulate import tabulate
from datetime import datetime


from logger import logger as Logger
from core import selenium, assertion
from report import report
from helpers import json_helper



def display_help():
    """Display help in a table format using tabulate."""
    # Define the parameters to show in the help table
    help_table = [
        ["-b, --browser", "Required", "Specify the browser to use, e.g., 'chrome', 'firefox'"],
        ["-s, --script", "Required", "Specify the source script, e.g., 'demo_source_workflow'"],
    ]
    # Print a neatly formatted help message
    print("Help for running the script:\n")
    print(tabulate(help_table, headers=["Parameter", "Required", "Description"], tablefmt="fancy_grid"))

    print("\nLog Levels Explanation:")
    log_help_table = [
        ["DEBUG", "Detailed information, typically useful only for diagnosing problems."],
        ["INFO", "General information about the program's execution."],
        ["WARNING", "Indicates something unexpected or problematic, but the program is still working."],
        ["ERROR", "Something went wrong, but the program is still running."],
        ["CRITICAL", "A very serious error that might prevent the program from continuing"],
    ]

    print(tabulate(log_help_table, headers=["Type", "Description"], tablefmt="fancy_grid"))

    print("\nExample usage:")
    print("  python run.py -b=chrome -s=demo_source_workflow")


def programHelper():
    parser = argparse.ArgumentParser(description="Run script with specified browser and source script", add_help=False)
    parser.add_argument('-b', '--browser', required=False, help="Specify the browser to use, e.g., 'chrome', 'firefox'")
    parser.add_argument('-s', '--script', required=False, help="Specify the source script, e.g., 'demo_source_workflow'")
    parser.add_argument('-h', '--help', action='store_true', help="Show this help message and exit")

    # Parse arguments
    args = parser.parse_args()

    # Display help if requested
    if args.help:
        display_help()
        sys.exit(0)

    # Set up the logger with the specified log level
    global logger
    logger = Logger.get_logger()
    # Check for required arguments and show custom error message if missing
    if not args.browser or not args.script:
        logger.error(
            "Error: Both -b (browser) and -s (source script) parameters are required.")
        display_help()
        sys.exit(1)

    # Display the parsed arguments (for demonstration purposes)
    logger.info(f"Browser: {args.browser}")
    logger.info(f"Source Script: {args.script}")
    return args.browser, args.script


def runScript(script_name):
    # Construct the full module path
    script_path = os.path.join("scripts", f"{script_name}.py")
    logger.info(f"Loading script: {script_name}")
 
    try:
        # Load the module using importlib
        spec = importlib.util.spec_from_file_location(script_name, script_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

    except FileNotFoundError:
        logger.error(f"script {script_name} not found at {script_path}.")
    except Exception as e:
        logger.error(f"An error occurred while running {script_name}: {e}")


if __name__ == "__main__":
    start = datetime.now()
    config = json_helper.loadJsonFile("config",None)
    browser, script = programHelper()

    driver = selenium.setup(browser=browser)
    runScript(script)
    
    selenium.teardown()

    assert_data = assertion.get_data()
    data = {
        "date": datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
        "tester":config['tester'],
        "test_cases": assert_data['test_cases'],
        "script":script,
        "browser":browser,
        "pass_count":assert_data['pass_count'],
        "fail_count":assert_data['fail_count'],
        "total":assert_data['pass_count']+assert_data['fail_count'],
        "execution_duration": (datetime.now() - start).total_seconds()
    }

    report.generate_report(data)

