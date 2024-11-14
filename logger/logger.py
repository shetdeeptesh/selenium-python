import logging
import coloredlogs
import os
from datetime import datetime
from utils import utils

_logger = None

def _setup_logger(level_name="INFO"):
    """Set up a logger with console and file handlers, with colorization in console."""
    global _logger
    _logger = logging.getLogger("CustomLogger")
    _logger.setLevel(getattr(logging, level_name.upper(), logging.INFO))  # Set log level

    # Log format with timestamp
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    date_format = "%Y-%m-%d %H:%M:%S"

    # Ensure the 'output' directory exists
    # output_dir = "output"
    # os.makedirs(output_dir, exist_ok=True)
    output_dir = utils.get_output_directory()
    filename = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    # Set up file handler with a timestamped filename
    log_filename = utils.join_filepath(filename, output_dir)
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.DEBUG)  # Capture all levels in the log file
    file_handler.setFormatter(logging.Formatter(log_format, date_format))

    # Set up console handler with colored output
    coloredlogs.install(level=level_name, logger=_logger, fmt=log_format, datefmt=date_format)

    # Add both handlers to the logger
    _logger.addHandler(file_handler)

    return _logger

def get_logger():
    """Return the configured logger instance."""
    if _logger is None:
        _setup_logger()
    return _logger
