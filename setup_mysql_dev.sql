-- Prepares a MySQL Server for this project.
-- Creates a new User and a new Database
-- Set ALL privileges on the Database `hbnb_dev_db` to the `hbnb_dev` User.
-- Set SELECT privileges on the Database `performance_schema` to the `hbnb_dev` User.


CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

