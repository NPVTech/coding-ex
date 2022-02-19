import datetime

from dataclasses import dataclass
from enum import Enum


class TargetAccount(Enum):
    YES = 'Yes'
    NO = 'No'


@dataclass
class Company:
    id: str
    name: str
    start_date: datetime.date
    logo_image_url: str
    employees: int
    target_account: TargetAccount
