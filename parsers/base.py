import json

from abc import ABC, abstractmethod


class JSONParser(ABC):

    @abstractmethod
    def get_model_class(self):
        pass

    @property
    @abstractmethod
    def parse_field_function_map(self):
        pass

    def parse_json(self, json_str):
        json_object = json.loads(json_str)
        fields = {k: self.parse_field(k, v) for k, v in json_object.items()}
        return self.get_model_class()(**fields)

    def parse_field(self, field_name, field_value):
        parse_func = self.parse_field_function_map.get(field_name, lambda value: value)
        return parse_func(field_value)
