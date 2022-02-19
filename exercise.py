import csv

from collections import defaultdict

from models.company import TargetAccount
from parsers.companies import CompanyParser
from parsers.opportunities import OpportunityParser
from utils.files_util import download_file, parse_json_file


def part_one():
    """
    Download csv files and write them as json.
    """
    download_file('https://pbryan.github.io/exercise/companies.csv', 'companies.json')
    download_file('https://pbryan.github.io/exercise/opportunities.csv', 'opportunities.json')


def part_two():
    """
    Read all json objects into collections of Python objects in memory.
    """
    companies = {}
    opportunities = {}
    opportunities_by_company = defaultdict(list)

    company_parser = CompanyParser()
    for company in parse_json_file('companies.json', company_parser):
        companies[company.id] = company
    
    opportunity_parser = OpportunityParser()
    for opportunity in parse_json_file('opportunities.json', opportunity_parser):
        opportunities[opportunity.id] = opportunity
        opportunities_by_company[opportunity.company_id].append(opportunity)

    return companies, opportunities, opportunities_by_company


def part_three(companies, opportunities_by_company):
    """
    From all data loaded into objects in memory, output a CSV file, containing:

    - company name
    - start date in mm/dd/yyyy format
    - total amount of opportunities
    - average opportunity amount
    - date of last opportunity update in mm/dd/yyyy format
    """
    with open('company_report.csv', 'w') as report_file:
        csv_writer = csv.writer(report_file, delimiter=',')
        for company in companies.values():
            company_opportunities = opportunities_by_company[company.id]

            company_name = company.name
            start_date = company.start_date
            amount_of_opportunities = len(company_opportunities)
            sum_opportunities_amount = sum(opportunity.amount for opportunity in company_opportunities)
            average_amount = sum_opportunities_amount / amount_of_opportunities
            last_opportunity_date = max(company_opportunities, key=lambda opportunity: opportunity.updated_at).updated_at

            report_row = [
                company_name,
                start_date.strftime("%m/%d/%Y"),
                amount_of_opportunities,
                average_amount,
                last_opportunity_date.strftime("%m/%d/%Y")
            ]

            csv_writer.writerow(report_row)


def part_four(companies, opportunities_by_company):
    """
    From all data loaded into objects in memory, output a CSV file that summarizes for target accounts and non-target accounts:

    - total opportunity amount
    - average opportunity amount
    """
    target_account_opportunities_amount = 0
    target_account_opportunities_amount_sum = 0

    non_target_account_opportunities_amount = 0
    non_target_account_opportunities_amount_sum = 0

    for company in companies.values():
        company_opportunities = opportunities_by_company[company.id]
        opportunities_amount = sum(opportunity.amount for opportunity in company_opportunities)

        if company.target_account == TargetAccount.YES:
            target_account_opportunities_amount += 1
            target_account_opportunities_amount_sum += opportunities_amount

        else:
            non_target_account_opportunities_amount += 1
            non_target_account_opportunities_amount_sum += opportunities_amount

    with open('summary_report.csv', 'w') as report_file:
        target_account_row = [
            'target_accounts',
            target_account_opportunities_amount_sum,
            target_account_opportunities_amount_sum / target_account_opportunities_amount,
        ]

        non_target_account_row = [
            'non_target_accounts',
            non_target_account_opportunities_amount_sum,
            non_target_account_opportunities_amount_sum / non_target_account_opportunities_amount,
        ]

        report_rows = [
            target_account_row,
            non_target_account_row,
        ]

        csv_writer = csv.writer(report_file, delimiter=',')
        csv_writer.writerows(report_rows)


if __name__ == '__main__':
    part_one()
    companies, opportunities, opportunities_by_company = part_two()
    part_three(companies, opportunities_by_company)
    part_four(companies, opportunities_by_company)
