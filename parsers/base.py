import json

from abc import ABC, abstractmethod


class JSONParser(ABC):

    def parse_json(self, json_str):
        json_object = json.loads(json_str)
        fields = {k: self.parse_field(k, v) for k, v in json_object.items()}
        return self.get_model_class()(**fields)
    
    @abstractmethod
    def get_model_class(self):
        pass

    @abstractmethod
    def parse_field(self, field_name, field_value):
        pass
