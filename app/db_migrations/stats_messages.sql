-- Create the stats table
CREATE TABLE stats (
    id SERIAL PRIMARY KEY,
    customerId INTEGER NOT NULL,
    type VARCHAR NOT NULL,
    amount VARCHAR NOT NULL,
    uuid UUID NOT NULL
);

-- Create the customerId_stats table
CREATE TABLE customerId_stats (
    customerId INTEGER PRIMARY KEY,
    messageCount INTEGER NOT NULL DEFAULT 0,
    totalAmount NUMERIC(12, 3) NOT NULL DEFAULT 0.0
);

-- Create the messageType_stats table
CREATE TABLE messageType_stats (
    messageType VARCHAR PRIMARY KEY,
    messageCount INTEGER NOT NULL DEFAULT 0,
    totalAmount NUMERIC(12, 3) NOT NULL DEFAULT 0.0
);


-- Create the messageUuid_stats table
CREATE TABLE messageUuid_stats (
    messageUuid UUID PRIMARY KEY,
    customerId INTEGER NOT NULL,
    messageType VARCHAR NOT NULL,
    amount NUMERIC(12, 3) NOT NULL
);

-- Create the primary key index on the messageUuid_stats table
CREATE INDEX idx_messageUuid_stats ON messageUuid_stats (messageUuid);

-- Create the foreign key constraints
ALTER TABLE stats ADD CONSTRAINT fk_customerId_stats
    FOREIGN KEY (customerId)
    REFERENCES customerId_stats (customerId)
    ON UPDATE CASCADE
    ON DELETE CASCADE;

ALTER TABLE stats ADD CONSTRAINT fk_messageType_stats
    FOREIGN KEY (type)
    REFERENCES messageType_stats (messageType)
    ON UPDATE CASCADE
    ON DELETE CASCADE;

ALTER TABLE stats ADD CONSTRAINT fk_messageUuid_stats
    FOREIGN KEY (uuid)
    REFERENCES messageUuid_stats (messageUuid)
    ON UPDATE CASCADE
    ON DELETE CASCADE;
