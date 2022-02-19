from datetime import datetime

from models.company import Company, TargetAccount
from parsers.base import JSONParser


class CompanyParser(JSONParser):

    def get_model_class(self):
        return Company

    @property
    def parse_field_function_map(self):
        return {
            'target_account': lambda value: TargetAccount[value.upper()],
            'start_date': lambda value: datetime.strptime(value, "%Y-%m-%d").date()
        }
