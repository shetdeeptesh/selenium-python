# json_helper.py
import json
from utils import utils
from logger import logger as Logger

_logger = Logger.get_logger()

# Helper function to save a JSON file
def saveJsonFile(filename: str, data: any, location: str = None):
    try:
        filepath = utils.join_filepath(filename,location)
        file = utils.open_file(filepath, 'w')
        json.dump(data, file)
        _logger.info(f"JSON file saved successfully: {filepath}.json")
    except Exception as e:
        _logger.error(f"An error occurred while saving the JSON file: {e}")

# Helper function to load a JSON file

def loadJsonFile(filename: str, location: str = "data"):
    try:
        # Join the file path with the location
        filepath = filename+".json"

        if location is not None:
            filepath = utils.join_filepath(filepath, location)

        if filepath is None:
            return None

        # Read the JSON file
        file_data = utils.open_file(filepath, 'r')
        if file_data is None:
            return None
        
        data = json.loads(file_data)
        _logger.info(f"JSON file loaded successfully: {filepath}")
        return data
    
    except Exception as e:
        _logger.error(f"An error occurred while loading the JSON file: {e}")
        return None