import csv
import json
import urllib.request

from dataclasses import dataclass
from enum import Enum


class OpportunityStatus(Enum):
    PENDING = 'pending'
    ACTIVE = 'active'
    CLOSED = 'closed'


class OpportunityType(Enum):
    NEW_LOGO = 'new_logo'
    EXPANSION = 'expansion'
    OTHER = 'other'


def _str_to_oportunity_type_enum(str_type):
    return {
        'new_logo': OpportunityType.NEW_LOGO,
        'expansion': OpportunityType.EXPANSION,
        'other': OpportunityType.OTHER,
    }[str_type]


def _str_to_oportunity_status_enum(str_status):
    return {
        'pending': OpportunityStatus.PENDING,
        'active': OpportunityStatus.ACTIVE,
        'closed': OpportunityStatus.CLOSED,
    }[str_status]


@dataclass
class Company:
    id: int
    name: str
    start_date: str
    logo_image_url: str
    employees: int
    target_account: bool

    def __post_init__(self):
        # TODO: improve
        self.target_account = self.target_account == 'Yes'


def gen():
    for x in range(55):
        yield x


@dataclass
class Opportunity:
    id: int
    company_id: int
    amount: int
    type: OpportunityType
    updated_at: str  # TODO: timestamp in ISO 8601 format
    status: OpportunityStatus

    def __post_init__(self):
        # TODO: improve
        self.type = _str_to_oportunity_type_enum(self.type)
        self.status = _str_to_oportunity_status_enum(self.status)


def part_one():
    download_file('https://pbryan.github.io/exercise/companies.csv', 'companies.json')
    download_file('https://pbryan.github.io/exercise/opportunities.csv', 'opportunities.json')


def download_file(src_url, output_filename):
    csv_file_path, _ = urllib.request.urlretrieve(src_url)

    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with open(output_filename, mode='w') as json_file:
            for csv_row in csv_reader:
                json_row = {k: v for k, v in csv_row.items() if not k.startswith('_')}
                json.dump(json_row, json_file)
                json_file.write('\n')


def part_two():
    companies = {}
    for raw_company in _get_data_from_json_file('companies.json'):
        company = Company(**raw_company)
        companies[company.id] = company

    opportunities = {}
    for raw_opportunity in _get_data_from_json_file('opportunities.json'):
        opportunity = Opportunity(**raw_opportunity)
        opportunities[opportunity.id] = opportunity

    return companies, opportunities


def part_three(companies, opportunities):
    for company in companies:
        pass


def _get_data_from_json_file(file_name):
    with open(file_name, 'r') as json_file:
        rows = [json.loads(row) for row in json_file]
    return rows


if __name__ == '__main__':
    part_one()
    companies, opportunities = part_two()
    part_three(companies, opportunities)
