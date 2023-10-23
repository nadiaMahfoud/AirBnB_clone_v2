-- Creating a database named 'hbnb_test_db' if it does not already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Ensuring the changes take effect by refreshing the privileges 
FLUSH PRIVILEGES;

-- Creating a new MySQL user 'hbnb_test' with the password 'hbnb_test_pwd'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Granting all the privileges on the 'hbnb_test_db' to the 'hbnb_test' user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Granting "SELECT privilege" on 'performance_schema' to the 'hbnb_test' user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
