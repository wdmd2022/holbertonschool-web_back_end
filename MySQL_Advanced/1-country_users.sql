-- This SQL script creates a table `users` with the requirements:
-- Has these attributes:
-- * id: integer, never null, auto increment, primary key
-- * email: string (255 char), never null, unique
-- * name: string (255 char)
-- * country: enumeration of countries: `US`, `CO`, and `TN`, never null
-- i.e., default will be the first element of the enumeration, here `US`
-- if the table already exists, script should not fail
-- script can be executed on any database
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL
);
