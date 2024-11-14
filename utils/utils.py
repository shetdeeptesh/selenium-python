import os
import json
from datetime import datetime
import logging  # Use Python's logging directly in utils

# from logger import logger as Logger

_logger = logging.getLogger("CustomLogger")
_output_dir = None

def checkFilePath(file_path: str, create_if_missing: bool = False) -> bool:
    """
    Check if the given file path exists. If it's a directory, check if it exists; otherwise check if the file exists.
    """

    try:
        pass
        if create_if_missing:
            os.makedirs(file_path, exist_ok=True)
            _logger.info(f"Directory created: {file_path}")
        return os.path.exists(file_path)

    except Exception as e:
        _logger.error(f"An error occurred while checking the file path: {e}")
        return False




def open_file(file_path: str, mode='r', data=None):
    """
    Open a file in the specified mode and return its content or None.
    
    Parameters:
        file_path (str): The path to the file to open.
        mode (str): The mode to open the file in ('r' for read, 'w' for write, 'a' for append).
        data (str): The data to write to the file (if mode is 'w' or 'a').
    
    Returns:
        str: The content of the file if in read mode, or None if an error occurs.
    """
    try:
        # Open the file in the specified mode
        
        with open(file_path, mode) as f:
            if mode == 'r':  # Read file
                if checkFilePath(file_path):
                    return f.read() 
                _logger.error(f"File not found: {file_path}")

            elif mode in ['w', 'a'] and data is not None:  # Write or append data
                f.write(data)
                return True  # Indicating the write was successful
            else:
                _logger.error(f"Currently {mode} does not support.")
                raise TypeError(f"Unsupported mode: {mode}")
            
    except Exception as e:
        _logger.error(f"An error occurred while opening the file: {e}")
        return None


def join_filepath(file_path: str, location: str, create_if_missing: bool = False) -> str:
    """
    Join file_path with location and return the full path.
    """
    try:
        if location:
            full_path = os.path.join(location, file_path)
            if create_if_missing:
                checkFilePath(location, create_if_missing=True)
            return full_path
        else:
            _logger.error("Location is None, cannot join paths.")
            return file_path
    except Exception as e:
        _logger.error(f"An error occurred while joining filepath: {e}")
        return None

def get_output_directory() -> str:
    """
    Get the output directory path and create it if it doesn't exist.
    """
    global _output_dir
    if _output_dir is None:
        output_dir = "output"
        sub_folder = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        checkFilePath(output_dir, create_if_missing=True)
        output = join_filepath(sub_folder, output_dir, create_if_missing=True)
        
        if output and checkFilePath(output, create_if_missing=True):
            _output_dir = output
            return output
        else:
            _logger.error("Failed to create or retrieve the output directory.")
            _output_dir = output_dir
            return output_dir  
        
    return _output_dir