from configparser import ConfigParser

def get_config(section, key):
    config = ConfigParser()
    config.read('path/to/config.ini')  # Update with the correct path
    return config.get(section, key)
