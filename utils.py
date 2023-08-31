# Extermal modules
import os
from configparser import ConfigParser
from datetime import date
from pathlib import Path


def get_data_from_config(section, config_key):
    """Return some data from a given key in config.ini."""
    this_file = Path(__file__)
    ROOT_DIR = this_file.parent.absolute()
    config_path = os.path.join(ROOT_DIR, "config.ini")
    parser = ConfigParser()
    parser.read(config_path)
    data = parser.get(section, config_key)
    return data


def get_date():
    """Return today's date in danish format (dd-mm-yy)."""
    today = date.today()
    today = today.strftime("%d-%m-%Y")
    return today


def shorten_filename(filename):
    """Return a shortened version of a given filename (using the final component of the path)."""
    filenameShort = os.path.basename(filename)
    return filenameShort


def create_directory(path):
    """Create new folder path if it doesn't already exist."""
    if not os.path.exists(path):
        os.makedirs(path)
