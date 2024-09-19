import logging
import os


class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        # Create log directory if it doesn't exist
        if not os.path.exists('./logs'):
            os.makedirs('./logs')

        # File handler for logging to a file
        file_handler = logging.FileHandler('./logs/test.log')
        file_handler.setLevel(logging.INFO)

        # Console handler for logging to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Define a format for log messages
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger
