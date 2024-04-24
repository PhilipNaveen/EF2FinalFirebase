-- Access the ToyDB within the servers
USE toydb;

-- Continue
go

-- Create the 'cameras' table if it does not exist
IF NOT EXISTS
(
    SELECT *
    FROM information_schema.tables
    WHERE table_name = 'cameras'
)
BEGIN
    -- Table structure for table 'cameras'
    -- This table stores information about cameras
    CREATE TABLE cameras
    (
        -- Use the id (whatever this actually is) as the primary key
        id INT IDENTITY(1, 1) PRIMARY KEY,
        -- Unique serial number for each camera
        serial_no VARCHAR(255) NOT NULL,
        -- Short location description for each camera
        location_short VARCHAR(255) NOT NULL,
        -- Long location description for each camera
        location_long VARCHAR(255) NOT NULL,
        -- Timestamp for when the camera was created
        created_at DATETIME NOT NULL
    );
END

go

-- Create the 'rawmetrics' table if it does not exist
IF NOT EXISTS
(
    SELECT *
    FROM information_schema.tables
    WHERE table_name = 'rawmetrics'
)
BEGIN
    -- Table structure for table 'rawmetrics'
    -- This table stores raw metrics data
    CREATE TABLE rawmetrics
    (
        -- Unique identifier for each raw metric
        id INT IDENTITY(1, 1) PRIMARY KEY,
        -- Source of the raw metric
        source VARCHAR(255) NOT NULL,
        -- Unique serial number for each raw metric
        serial_no VARCHAR(255) NOT NULL,
        -- Occupancy level for the raw metric
        occupancy INT NOT NULL,
        -- Count of people entering the area
        count_in INT NOT NULL,
        -- Count of people leaving the area
        count_out INT NOT NULL,
        -- Unix timestamp for the raw metric
        source_unixtime BIGINT NOT NULL,
        -- Timestamp for when the raw metric was created
        created_at DATETIME NOT NULL
    );
END

go

-- Create the 'rawmetrics_occupancy' table if it does not exist
IF NOT EXISTS
(
    SELECT *
    FROM information_schema.tables
    WHERE table_name = 'rawmetrics_occupancy'
)
BEGIN
    -- Table structure for table 'rawmetrics_occupancy'
    -- This table stores occupancy data
    CREATE TABLE rawmetrics_occupancy
    (
        -- Unique identifier for each occupancy record
        id INT IDENTITY(1, 1) PRIMARY KEY,
        -- Unique serial number for each occupancy record
        serial_no VARCHAR(255) NOT NULL,
        -- Occupancy level for the record
        occupancy INT NOT NULL,
        -- Total number of people entering the area
        total_in INT NOT NULL,
        -- Total number of people leaving the area
        total_out INT NOT NULL,
        -- Date of the occupancy record
        date DATE NOT NULL,
        -- Time of the occupancy record
        [time] TIME NOT NULL,
        -- Day of the week of the occupancy record
        [day] VARCHAR(255) NOT NULL,
        -- Day of the week abbreviation of the occupancy record
        dow VARCHAR(255) NOT NULL
    );
END

go

-- Create the 'rawmetrics_sum' table if it does not exist
IF NOT EXISTS
(
    SELECT *
    FROM information_schema.tables
    WHERE table_name = 'rawmetrics_sum'
)
BEGIN
    -- Table structure for table 'rawmetrics_sum'
    -- This table stores summed raw metrics data
    CREATE TABLE rawmetrics_sum
    (
        -- Unique identifier for each summed raw metric
        id INT IDENTITY(1, 1) PRIMARY KEY,
        -- Unique serial number for each summed raw metric
        serial_no VARCHAR(255) NOT NULL,
        -- Total number of people entering the area
        count_in INT NOT NULL,
        -- Total number of people leaving the area
        count_out INT NOT NULL,
        -- Date of the summed raw metric
        [date] DATE NOT NULL,
        -- Time of the summed raw metric
        [time] TIME NOT NULL,
        -- Day of the week of the summed raw metric
        [day] VARCHAR(255) NOT NULL,
        -- Day of the week abbreviation of the summed raw metric
        dow VARCHAR(255) NOT NULL
    );
END

go