import json

class JsonConfigurator:
    def __init__(self, file_path: str):
        """""" 
        self.path = file_path
        self.configs: dict = self.load_source(path = file_path)

    def load_source(self, path: str)-> dict:
        with open(path) as f:
            configurations = json.load(f)
        return configurations
    
    def get_value(self, key)-> str:
        return self.configs[key]