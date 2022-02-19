from datetime import datetime

from models.opportunity import Opportunity, OpportunityStatus, OpportunityType
from parsers.base import JSONParser


class OpportunityParser(JSONParser):

    def get_model_class(self):
        return Opportunity
    
    @property
    def parse_field_function_map(self):
        return {
            'type': lambda value: OpportunityType[value.upper()],
            'status': lambda value: OpportunityStatus[value.upper()],
            'amount': lambda value: int(value),
            'updated_at': lambda value: datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
        }
