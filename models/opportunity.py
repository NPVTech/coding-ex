from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class OpportunityStatus(Enum):
    PENDING = 'pending'
    ACTIVE = 'active'
    CLOSED = 'closed'


class OpportunityType(Enum):
    NEW_LOGO = 'new_logo'
    EXPANSION = 'expansion'
    OTHER = 'other'


@dataclass
class Opportunity:
    id: str
    company_id: int
    amount: int
    type: OpportunityType
    updated_at: datetime
    status: OpportunityStatus
