/*here i created the table with 3 variables server_id, timeofreading, temperature*/
CREATE TABLE readings_dataset (
    server_id INT,
    timeofreading DATETIME,
    temperature DECIMAL(10,2),
    PRIMARY KEY (cage_id, dateofreading),
    INDEX (dateofreading, cage_id) -- suggested index, useful for time-based queries
)
