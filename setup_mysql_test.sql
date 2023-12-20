-- prepares a MySQL server for the project
-- all privileges on the database hbnb_test_db
-- privilege on the database performance_schema
-- new user hbnb_test (in localhost)

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';

SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';

USE hbnb_test_db;
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
