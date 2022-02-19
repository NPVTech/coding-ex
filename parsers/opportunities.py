from datetime import datetime

from models.opportunity import Opportunity, OpportunityStatus, OpportunityType
from parsers.base import JSONParser


class OpportunityParser(JSONParser):

    STR_TO_STATUS_MAP = {
        'pending': OpportunityStatus.PENDING,
        'active': OpportunityStatus.ACTIVE,
        'closed': OpportunityStatus.CLOSED,
    }

    STR_TO_TYPE_MAP = {
        'new_logo': OpportunityType.NEW_LOGO,
        'expansion': OpportunityType.EXPANSION,
        'other': OpportunityType.OTHER,
    }

    def get_model_class(self):
        return Opportunity

    def parse_field(self, field_name, field_value):
        if field_name == 'type':
            return self.STR_TO_TYPE_MAP[field_value]
        if field_name == 'status':
            return self.STR_TO_STATUS_MAP[field_value]
        if field_name == 'amount':
            return int(field_value)
        if field_name == 'updated_at':
            return datetime.strptime(field_value, '%Y-%m-%dT%H:%M:%SZ')
        return field_value
