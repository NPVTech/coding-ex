CREATE TABLE Company (
    id VARCHAR(36) NOT NULL,
    name VARCHAR(255),
    start_date VARCHAR(10),
    logo_image_url VARCHAR(255),
    employees INT,
    target_account VARCHAR(3),
    PRIMARY KEY (id),
);


CREATE INDEX idx_company
ON Company(id);


CREATE TABLE Opportunity (
    id VARCHAR(36) NOT NULL,
    company_id VARCHAR(36) NOT NULL,
    amount int,
    type VARCHAR(10),
    updated_at VARCHAR(20),
    status VARCHAR(10),
    PRIMARY KEY (id),
    FOREIGN KEY (company_id) REFERENCES Company(id)
);


CREATE INDEX idx_opportunity
ON Opportunity(id);
