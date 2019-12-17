import logging


class GlobalConfig():
    def __init__(self):
        self.logger = ""
        self.log_file = ""

    def get_logger(self):
        self.logger = logging.getLogger('ML Model - classification')
        self.logger.setLevel(logging.INFO)
        log_file_handler = logging.FileHandler(self.log_file)
        log_file_handler.setLevel(logging.INFO)
        logging_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_file_handler.setFormatter(logging_formatter)
        self.logger.addHandler(log_file_handler)
        return self.logger
