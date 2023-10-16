-- Write an SQL script that creates a table `users` as follows:
-- with these attributes:
-- * id, integer, never null, auto increment, primary key
-- * email, string (255 characters), never null, unique
-- * name, string (255 characters)
-- if the table already exists, the script should not fail
-- the script can be executed on any database
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
