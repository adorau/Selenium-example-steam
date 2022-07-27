import json
from singleton import Singleton


class ConfigManager(metaclass=Singleton):
    def __init__(self):
        self.config = None
        self.load_config()

    def load_config(self):
        with open ('config.json', "r") as config_file:
            self.config = json.load(config_file)
