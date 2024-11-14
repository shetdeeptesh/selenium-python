from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from xhtml2pdf import pisa
from utils import utils

import logging  # Use Python's logging directly in utils

_logger = logging.getLogger("CustomLogger")



def generate_report(data: dict = None):
    # Data for the report
    _logger.info("Generating Report")
    # Set up the Jinja environment
    env = Environment(loader=FileSystemLoader('report'))  # Assume 'templates' is the folder where your template is
    template = env.get_template('report_template.html')

    # Render the HTML with the provided data
    html_content = template.render(data)

    # Ensure the output directory exists
    output_dir = utils.get_output_directory()
    filename = "report.html"
    output_file = utils.join_filepath(filename, output_dir)

    # Ensure file creation
    if utils.open_file(output_file, "w", html_content):
        _logger.info("Report generated successfully!")
    else:
        _logger.error("Error generating report!")