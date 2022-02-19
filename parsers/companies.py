from datetime import datetime

from models.company import Company, TargetAccount
from parsers.base import JSONParser


class CompanyParser(JSONParser):

    STR_TO_TARGET_MAP = {
        'Yes': TargetAccount.YES,
        'No': TargetAccount.NO,
    }

    def get_model_class(self):
        return Company

    def parse_field(self, field_name, field_value):
        if field_name == 'target_account':
            return self.STR_TO_TARGET_MAP[field_value]
        if field_name == 'start_date':
            return datetime.strptime(field_value, "%Y-%m-%d").date()
        return field_value
