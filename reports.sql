# Companies report
SELECT Company.name, Company.start_date, SUM(Opportunity.amount), AVG(Opportunity.amount), MAX(Opportunity.updated_at) FROM Company
LEFT JOIN Opportunity ON Opportunity.company_id = Company.id
GROUP BY Company.target_account;


# Summary report
SELECT Company.target_account, SUM(Opportunity.amount), AVG(Opportunity.amount) FROM Company
LEFT JOIN Opportunity ON Opportunity.company_id = Company.id
GROUP BY Company.target_account;
